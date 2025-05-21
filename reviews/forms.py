from django.forms import ModelForm, Textarea, TextInput
from reviews.models import Review 


class ReviewForm(ModelForm):
    class Meta():
        model = Review
        fields = [ "first_name", "last_name", "email",  "comments" ]
        widgets = {
            "first_name": TextInput(attrs={'autofocus': True}),
            "last_name": TextInput(),
            "comments": Textarea(),
        }

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(
#         widget=forms.TextInput(attrs={'autofocus': True})
#     )
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     comments = forms.CharField(
#         widget=forms.Textarea()
#     )