from django.urls import path
from games.views import MathFactsView, AnagramHuntView, record_final_score


app_name = 'games'


urlpatterns = [
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path("record-final-score", record_final_score, name="record-score"),
]