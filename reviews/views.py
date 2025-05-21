from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from reviews.forms import ReviewForm


class ReviewFormView(FormView):
    template_name = "reviews/review-form.html"
    form_class = ReviewForm
    success_url = reverse_lazy("reviews:thanks")


class ReviewThanksView(TemplateView):
    template_name = "reviews/thanks.html"