from django.urls import path
from users.views import CustomPasswordChangeView, MyAccountView


urlpatterns = [
    path("password/change/", CustomPasswordChangeView.as_view(),name="account_change_password"),
    path("my-account/", MyAccountView.as_view(), name="my-account"),
]