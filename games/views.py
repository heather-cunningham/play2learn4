import json
from django.http import JsonResponse
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView
from games.models import FinalScore, Game


## CBVs: Class-based Views
class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class AHLeaderboardView(ListView): ## Anagram Hunt Leaderboard
    model = FinalScore
    template_name = "games/ah-leaderboard.html"
    context_object_name = "anagram_scores"
    #
    #
    def get_queryset(self):
        anagram_scores_qryset = FinalScore.objects.filter(game__game_name="anagram_hunt").order_by("-final_score")
        for score in anagram_scores_qryset:
            localized_dt = localtime(score.game_date_time).strftime("%m/%d/%Y %I:%M %p %Z")
            date, time, am_pm_mark, timezone = localized_dt.split(" ")
            score.game_date_time = f"{date} {time}{am_pm_mark.lower()} {timezone}"
        return anagram_scores_qryset


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class MFLeaderboardView(ListView): ## Math Facts Leaderboard
    model = FinalScore
    template_name = "games/mf-leaderboard.html"
    context_object_name = "math_scores"
    #
    #
    def get_queryset(self):
        math_scores_qryset = FinalScore.objects.filter(game__game_name="math_facts").order_by("-final_score")
        for score in math_scores_qryset:
            localized_dt = localtime(score.game_date_time).strftime("%m/%d/%Y %I:%M %p %Z")
            date, time, am_pm_mark, timezone = localized_dt.split(" ")
            score.game_date_time = f"{date} {time}{am_pm_mark.lower()} {timezone}"
        return math_scores_qryset


## Function-based Views
## --------------------
@csrf_exempt  # Remove this once authentication is set up properly and add `@csrf_protect`. Players will have to log in to play games.
@require_http_methods(["POST"])
def create_game(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        game = Game.objects.create(
            game_name=data["game_name"],
            settings=data["settings"]
        )
        return JsonResponse({"status": "success", "game_id": game.id, "message": "Game created!"})
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)
    except Exception as e:
        return JsonResponse({"status": "Error - Game not created.", "message": str(e)}, status=400)


# @login_required
# @csrf_protect
@csrf_exempt  # Remove this once authentication is set up properly and add `@csrf_protect`
@require_http_methods(["POST"])
def submit_final_score(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        ## Ensure all the req'd fields are in the data:
        if ("game_id" not in data or "game_name" not in data or "settings" not in data 
            or "final_score" not in data):
                return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)
        game = get_object_or_404(Game, id=int(data["game_id"]))
        # Ensure final_score is valid
        final_score = data.get("final_score")
        if (final_score is None):  
            return JsonResponse(
                {"status": "error", 
                 "message": "final_score == None, Null, or its value is otherwise missing"},
                status=400)
        ## Handle authentication - use test user for now if request.user is not authenticated.  
        # Replace with actual authentication later.
        player = request.user if request.user.is_authenticated else None
        if (not player):
            User = get_user_model()
            player, created = User.objects.get_or_create(username="test_user") ## Rtns tple of (Obj, Boolean)
            if (created):
                player.set_password("password123")  
                player.save()
        final_score_obj = FinalScore.objects.create(
            player=player,
            game=game,
            # game_id=data["game_id"],
            game_name=data["game_name"],
            final_score=final_score,
            settings=json.dumps(data["settings"])
        )
        if (final_score_obj):
            final_score_obj.save()
        return JsonResponse({"status": "success", "message": "Score saved!"})
    except json.JSONDecodeError as e:
        return JsonResponse({"status": "error", "message": f"Invalid JSON format: {str(e)}"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)
## END fcnal view: submit_final_score()