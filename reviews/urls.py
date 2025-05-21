from django.urls import path
from reviews.views import ReviewFormView, ReviewThanksView


app_name = "reviews"


urlpatterns = [
    path("reviews/", ReviewFormView.as_view(), name="feedback"),
    path("reviews/thanks/", ReviewThanksView.as_view(), name="thanks"),
]