from django.urls import path
from pages.views import AboutUsView, HomePageView


app_name = "pages"


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutUsView.as_view(), name="about"),
]