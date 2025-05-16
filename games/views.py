import json
from django.http import JsonResponse
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
    template_name = "games/ah_leaderboard.html"
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
    template_name = "games/mf_leaderboard.html"
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
        json_response = JsonResponse({"status": "success", "game_id": game.id, "message": "Game created!"})
        print(json_response) 
        return json_response
    except json.JSONDecodeError:
        json_response = JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)
        print(json_response) 
        return json_response
    except Exception as e:
        json_response = JsonResponse({"status": "Error - Game not created.", "message": str(e)},
                                      status=400)
        print(json_response) 
        return json_response



@csrf_exempt  # Remove this once authentication is set up properly and add `@csrf_protect`
@require_http_methods(["POST"])
def submit_final_score(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        
        # Find the correct game instance
        game = Game.objects.get(game_name=data["game_name"])

        # Save the player's score for this game session
        FinalScore.objects.create(
            player=request.user,
            game=game,
            final_score=data["final_score"]
        )

        return JsonResponse({"status": "success", "message": "Score saved!"})

    except Game.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Game not found."}, status=404)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)


# @login_required
# @csrf_protect
# @csrf_exempt  # Remove this once authentication is set up properly and add `@csrf_protect`
# @require_http_methods(["POST"])
# def submit_final_score(request):
#     """ Submit/send the final score and info of a game to the backend. """
#     try:
#         data = json.loads(request.body.decode("utf-8"))
#         # Validate required fields
#         required_fields = ["game_name", "final_score"]
#         for field in required_fields:
#             if (field not in data):
#                 return JsonResponse({"status": "error", "message": f"Missing field: `{field}`."}, status=400)
#         # Ensure game_name is valid
#         game_name = data.get("game_name")
#         if (game_name not in dict(Game.GAME_NAME_CHOICES).keys()):
#             return JsonResponse({"status": "error", "message": "Invalid game_name."}, status=400)
#         # Ensure final_score is valid
#         final_score = data.get("final_score")
#         if (not final_score):  # if final_score is None or falsy
#             return JsonResponse(
#                 {"status": "error", 
#                  "message": "final_score == None, Null, or its value is otherwise missing"},
#                 status=400)
#         # Retrieve the correct Game instance 
#         game = Game.objects.get(game_name=data["game_name"])
#         # Handle authentication - use test user for now if request.user is not authenticated.  
#         # Replace with actual authentication later.
#         player = request.user if request.user.is_authenticated else None
#         if (not player):
#             ## Get test_user for now, and if no test_user, create new one to use for now:
#             player, created = User.objects.get_or_create(username="test_user") ## Rtns a tuple 
#             if (created): ## created is True
#                 player.set_password("password123")  # Assign a basic password for testing
#                 player.save()
#         # Create and save the FinalScore obj
#         final_score_obj = FinalScore.objects.create(
#             player=player,
#             game=game,
#             final_score=final_score
#             # Do NOT include game_date_time. Django handles this automatically in the model. 
#             # Adding it here will interfere w/ that automatic date handling.  
#         )
#         final_score_obj.save()
#         json_response = JsonResponse(
#             {"status": "Success - final score info saved successfully",
#              "id": final_score_obj.id}, 
#              status=200)
#         print(json_response) 
#         return json_response
#     except json.JSONDecodeError:
#         json_response = JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)
#         print(json_response) 
#         return json_response
#     except Exception as e:
#         json_response = JsonResponse({"status": "Error - final score info not saved", "message": str(e)}, status=400)
#         print(json_response) 
#         return json_response
## END fcnal view: submit_final_score()