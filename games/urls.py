from django.urls import path
from games.views import AnagramHuntView, GameScoresView, MathFactsView, record_score


app_name = 'games'


urlpatterns = [
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path("record-score/", record_score, name="record-score"),
    path("game-scores/", GameScoresView.as_view(), name="game-scores"),
]