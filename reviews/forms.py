from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    comments = forms.CharField()