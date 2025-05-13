import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from games.models import GameFinalScore


class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


## Functions
def record_final_score(request):
    score_data = json.loads(request.body)
    username = score_data["username"]
    game_name = score_data["game_name"]
    final_score = score_data["final_score"]
    game_datetime = score_data["game_datetime"]
    new_score = GameFinalScore(username=username, game_name=game_name, final_score=final_score, 
                          game_datetime=game_datetime)
    new_score.save()
    #
    response = { "success": True }
    return JsonResponse(response)