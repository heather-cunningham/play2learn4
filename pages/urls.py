from django.urls import path
from pages.views import AboutUsView, ContactUsFormView, ContactUsThanksView, HomePageView


app_name = "pages"


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home/", HomePageView.as_view(), name="home"),
    path("about/", AboutUsView.as_view(), name="about"),
    path("contact-us/", ContactUsFormView.as_view(),  name="contact-us"),
    path("contact-thanks/", ContactUsThanksView.as_view(), name="contact-thanks"),
]