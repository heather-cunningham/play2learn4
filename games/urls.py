from django.urls import path
from games.views import (AnagramHuntView, AHLeaderboardView, MathFactsView, MFLeaderboardView, create_game,
                          submit_final_score)


app_name = 'games'


urlpatterns = [
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path("create-game/", create_game, name="create-game"),
    path("submit-final-score/", submit_final_score, name="submit-final-score"),
    path("ah-leaderboard/", AHLeaderboardView.as_view(), name="ah-leaderboard"),
    path("mf-leaderboard/", MFLeaderboardView.as_view(), name="mf-leaderboard"),
]