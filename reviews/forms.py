from django.forms import ModelForm, Textarea, TextInput
from reviews.models import Review 


class ReviewForm(ModelForm):
    class Meta():
        model = Review
        fields = [ "first_name", "last_name", "email", "username",  "comments" ]
        widgets = {
            "first_name": TextInput(attrs={'autofocus': True}),
            "last_name": TextInput(),
            "username": TextInput(),
            "comments": Textarea(),
        }