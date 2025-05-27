from django.urls import path
from users.views import MyAccountView


urlpatterns = [
    path("my-account/", MyAccountView.as_view(), name="my-account"),
]