import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView
from games.models import FinalScore


## CBVs: Class-based Views
class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class MFLeaderboardView(ListView): ## Math Facts Leaderboard
    model = FinalScore
    template_name = "games/mf_leaderboard.html"
    context_object_name = "math_scores"
    #
    def get_queryset(self):
        math_scores_qryset = FinalScore.objects.filter(game_name="math_facts").order_by("-final_score")
        for score in math_scores_qryset:
            localized_dt = localtime(score.game_date_time).strftime("%m/%d/%Y %I:%M %p %Z")
            date, time, am_pm_mark, timezone = localized_dt.split(" ")
            score.game_date_time = f"{date} {time}{am_pm_mark.lower()} {timezone}"
        return math_scores_qryset


class AHLeaderboardView(ListView): ## Anagram Hunt Leaderboard
    model = FinalScore
    template_name = "games/ah_leaderboard.html"
    context_object_name = "anagram_scores"
    #
    def get_queryset(self):
        anagram_scores_qryset = FinalScore.objects.filter(game_name="anagram_hunt").order_by("-final_score")
        for score in anagram_scores_qryset:
            localized_dt = localtime(score.game_date_time).strftime("%m/%d/%Y %I:%M %p %Z")
            date, time, am_pm_mark, timezone = localized_dt.split(" ")
            score.game_date_time = f"{date} {time}{am_pm_mark.lower()} {timezone}"
        return anagram_scores_qryset


## Function-based Views
# @login_required
# @csrf_protect
@csrf_exempt  # Remove this once authentication is set up properly and add `@csrf_protect`
@require_http_methods(["POST"])
def submit_final_score(request):
    """ Submit/send the final score and info of a game to the backend. """
    try:
        data = json.loads(request.body.decode("utf-8"))
        # Validate required fields
        required_fields = ["game_name", "final_score"]
        for field in required_fields:
            if (field not in data):
                return JsonResponse({"status": "error", "message": f"Missing field: `{field}`."}, status=400)
        # Ensure game_name is valid
        if (data["game_name"] not in dict(FinalScore.GAME_NAME_CHOICES)):
            return JsonResponse({"status": "error", "message": "Invalid game_name."}, status=400)
        game_name = data.get("game_name")
        final_score = data.get("final_score")
        # if (final_score is None):
        if (not final_score):
            return JsonResponse(
                {"status": "error", 
                 "message": "final_score == None, Null, or its value is otherwise missing"},
                status=400)
        # Handle authentication - use test user for now if request.user is not authenticated.  
        # Replace with actual authentication later.
        player = request.user if request.user.is_authenticated else None
        if (not player):
            ## Get test_user for now, and if no test_user, create new one to use for now:
            player, created = User.objects.get_or_create(username="test_user") ## Rtns a tuple 
            if (created): ## created is True
                player.set_password("password123")  # Assign a basic password for testing
                player.save()
        settings = data.get("settings", {})
        #
        final_score_obj = FinalScore.objects.create(
            game_name=game_name,
            player=player,
            settings=settings,
            final_score=final_score
            # Do NOT include game_date_time. Django handles this automatically in the model. 
            # Adding it here will interfere w/ that automatic date handling.  
        )
        final_score_obj.save()
        json_response = JsonResponse(
            {"status": "Success - final score info saved successfully",
             "id": final_score_obj.id}, 
             status=200)
        print(json_response) 
        return json_response
    except json.JSONDecodeError:
        json_response = JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)
        print(json_response) 
        return json_response
    except Exception as e:
        json_response = JsonResponse({"status": "Error - final score info not saved", "message": str(e)}, status=400)
        print(json_response) 
        return json_response
## END fcnal view: submit_final_score()