from django.urls import path
from games.views import (AnagramHuntView, AHLeaderboardView, MathFactsView, MFLeaderboardView, MyGamesView,
                         create_game, submit_final_score)


app_name = 'games'


urlpatterns = [
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path("create-game/", create_game, name="create-game"),
    # path("check-auth-status/", check_auth_status, name="check-auth-status"),
    path("submit-final-score/", submit_final_score, name="submit-final-score"),
    path("ah-leaderboard/", AHLeaderboardView.as_view(), name="ah-leaderboard"),
    path("mf-leaderboard/", MFLeaderboardView.as_view(), name="mf-leaderboard"),
    path("mf-leaderboard/", MFLeaderboardView.as_view(), name="mf-leaderboard"),
    path("my-games/", MyGamesView.as_view(), name="my-games"),
]