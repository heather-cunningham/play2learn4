import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from games.models import GameScore


class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class GameScoresView(TemplateView):
    template_name = "games/game-scores.html"
    #
    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        # context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context


## Functions
def record_score(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))  # Decoding for safety
            #
            user_name = data["user-name"]
            game = data["game"]
            score = data["score"]
            #
            new_score = GameScore(user_name=user_name, game=game, score=score)
            new_score.save()
            #
            # response = { 
            #     "success": True 
            # }
            return JsonResponse({"message": "Received data", "data": data})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "GET method not supported for this view"}, status=405)


# def record_score(request):
#     data = json.loads(request.body)
#     #
#     user_name = data["user-name"]
#     game = data["game"]
#     score = data["score"]
#     #
#     new_score = GameScore(user_name=user_name, game=game, score=score)
#     new_score.save()
#     #
#     response = { 
#         "success": True 
#     }
#     return JsonResponse(response)