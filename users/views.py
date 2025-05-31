from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from allauth.account.views import PasswordChangeView
from users.forms import CustomUserChangeForm


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("my-account")


class MyAccountView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = "account/my_account.html"
    #
    #
    ## @override
    def get_object(self):
        return self.request.user