from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from allauth.account.views import PasswordChangeView
from users.forms import CustomUserChangeForm


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("my-account")


class MyAccountView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = "Account/profile updated successfully!"
    template_name = "account/my_account.html"
    #
    #
    ## @override
    def get_object(self):
        return self.request.user
    #
    # @override
    def form_invalid(self, form):
        error_message = "Error updating account/profile."
        messages.error(self.request, error_message)
        return super().form_invalid(form)
