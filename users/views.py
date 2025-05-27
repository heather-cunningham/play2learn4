from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from users.forms import CustomUserChangeForm


class MyAccountView(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = "account/my_account.html"
    #
    #
    ## @override
    def get_object(self):
        return self.request.user