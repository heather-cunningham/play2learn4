import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from common.utils.email import send_email
from reviews.forms import ReviewForm

## BEGIN class
class ReviewFormView(FormView):
    template_name = "reviews/review-form.html"
    form_class = ReviewForm
    success_url = reverse_lazy("reviews:thanks")


    def form_valid(self, form):
        data = form.cleaned_data
        to = "cunningham.heatherirene@gmail.com"
        subject = "Review submitted"
        content = f'''<p>Hey PR Manager!</p>
            <p>Play2Learn feedback received:</p>
            <ul>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>' 
        content += '</ul>'
        send_email(to, subject, content)
        return super().form_valid(form)
## END class ReviewFormView


class ReviewThanksView(TemplateView):
    template_name = "reviews/thanks.html"