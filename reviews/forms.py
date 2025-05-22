from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.forms import ModelForm, CharField, Textarea, TextInput
from reviews.models import Review 


class ReviewForm(ModelForm):
    comments = CharField(
        validators=[
            MaxLengthValidator(2000),
            MinLengthValidator(10),
        ], 
        widget=Textarea(
            attrs={
                'maxlength': 2000,
                'required': True,
            }
        ),
        help_text="(Min: 10 characters, Max: 2000 characters)"
    )# end charfield
     

    class Meta():
        model = Review
        fields = [ "first_name", "last_name", "email", "username",  "comments" ]
        widgets = {
            "first_name": TextInput(attrs={
                'autofocus': True,
                'maxlength': 100,
                'required': True
                }),
            "last_name": TextInput(attrs={
                'maxlength': 100,
                'required': True
                }),
            "email": TextInput(attrs={
                'placeholder': "example@mail.com",
                'required': True
                }),
            "username": TextInput(),
        }
## END class ReviewForm