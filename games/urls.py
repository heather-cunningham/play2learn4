from django.urls import path
from games.views import AnagramHuntView, MathFactsView, MFLeaderboardView, submit_final_score


app_name = 'games'


urlpatterns = [
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path("submit-final-score/", submit_final_score, name="submit-final-score"),
    path("mf_leaderboard/", MFLeaderboardView.as_view(), name="mf_leaderboard"),
]