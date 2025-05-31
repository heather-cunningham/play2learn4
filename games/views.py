import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView
from games.models import FinalScore, Game


## ---------------------------------------------------------------------------------------------------
## Helper Fcns & Vars
## ---------------------------------------------------------------------------------------------------
def format_time_in_scores(scores_qryset):
    for score in scores_qryset:
        localized_dt = localtime(score.game_date_time).strftime("%m/%d/%Y %I:%M %p %Z")
        date, time, am_pm_mark, timezone = localized_dt.split(" ")
        score.game_date_time = f"{date} {time}{am_pm_mark.lower()} {timezone}"
    return scores_qryset

@login_required
def update_rankings(game_name):
    scores = FinalScore.objects.filter(game__game_name=game_name).order_by("-final_score")
    for index, score in enumerate(scores, start=1):
        score.rank = index
        score.save(update_fields=["rank"])


default_order = "rank"
def get_order_fields():
    return ["rank", "-rank", "player__username", "-player__username",
            "final_score", "-final_score", "game_date_time", "-game_date_time"]


## ---------------------------------------------------------------------------------------------------
## CBVs: Class-based Views
## ---------------------------------------------------------------------------------------------------
class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class AHLeaderboardView(ListView): ## Anagram Hunt Leaderboard
    model = FinalScore
    template_name = "games/ah-leaderboard.html"
    context_object_name = "anagram_scores"
    paginate_by = 10
    #
    # @override
    def get_ordering(self):
        ordering = self.request.GET.get("order", default_order)
        return ordering if ordering in get_order_fields() else default_order
    #
    # @override
    def get_queryset(self):
        ordering = self.get_ordering()
        anagram_scores_qryset = FinalScore.objects.filter(game__game_name="anagram_hunt").order_by(ordering)
        anagram_scores_qryset = format_time_in_scores(anagram_scores_qryset)
        return anagram_scores_qryset


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class MFLeaderboardView(ListView): ## Math Facts Leaderboard
    model = FinalScore
    template_name = "games/mf-leaderboard.html"
    context_object_name = "math_scores"
    paginate_by = 10
    #
    # @override
    def get_ordering(self):
        ordering = self.request.GET.get("order", default_order)
        return ordering if ordering in get_order_fields() else default_order
    #
    # @override
    def get_queryset(self):
        ordering = self.get_ordering()
        math_scores_qryset = FinalScore.objects.filter(game__game_name="math_facts").order_by(ordering)
        math_scores_qryset = format_time_in_scores(math_scores_qryset)
        return math_scores_qryset
    

class MyGamesView(LoginRequiredMixin, ListView):
    model = FinalScore
    template_name = "games/my-games.html"
    context_object_name = "my_scores"
    #
    # @override
    def get_ordering(self, table_type):
        # default_order = "-final_score"  
        ordering = self.request.GET.get(f"{table_type}_order", default_order)
        return ordering if ordering in get_order_fields() else default_order
    #
    ## @override
    def get_queryset(self):
        my_scores = FinalScore.objects.filter(player=self.request.user)
        my_scores = format_time_in_scores(my_scores)
        return my_scores
    #
    ## @override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Separate scores by game type, applying independent sorting
        ah_ordering = self.get_ordering("ah")
        mf_ordering = self.get_ordering("mf")
        #
        ah_scores_list = context["my_scores"].filter(game__game_name="anagram_hunt").order_by(ah_ordering)
        mf_scores_list = context["my_scores"].filter(game__game_name="math_facts").order_by(mf_ordering)
        # Pagination for Anagram Hunt Scores
        ah_paginator = Paginator(ah_scores_list, 5)  
        ah_page_number = self.request.GET.get("ah_page", 1)
        context["my_ah_scores"] = ah_paginator.get_page(ah_page_number)
        # Pagination for Math Facts Scores
        mf_paginator = Paginator(mf_scores_list, 5)  
        mf_page_number = self.request.GET.get("mf_page", 1)
        context["my_mf_scores"] = mf_paginator.get_page(mf_page_number)
        return context

    
## ---------------------------------------------------------------------------------------------------
## Function-based Views
## ---------------------------------------------------------------------------------------------------
@csrf_protect  
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
    
    
@csrf_protect
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
        # Check if the user is authenticated
        player = request.user if request.user.is_authenticated else None
        if (player is None):
            return JsonResponse({
                "status": "error",
                "message": "Please, log in or register to save your score!",
                "login_url": reverse("account_login"),  
                "signup_url": reverse("account_signup"), 
            }, status=401)
        game_name = data.get("game_name")
        ## Save score
        final_score_obj = FinalScore.objects.create(
            player=request.user,
            game=game,
            game_name=game_name,
            final_score=final_score,
            settings=json.dumps(data["settings"])
        )
        if (final_score_obj):
            final_score_obj.save()
        ## Set rank
        update_rankings(game_name)
        return JsonResponse({"status": "success", "message": "Score saved!"})
    except json.JSONDecodeError as e:
        return JsonResponse({"status": "error", "message": f"Invalid JSON format: {str(e)}"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)
## END fcnal view: submit_final_score()