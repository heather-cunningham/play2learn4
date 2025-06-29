import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from common.utils.email import send_email
from reviews.forms import ReviewForm


class ReviewFormView(FormView):
    template_name = "reviews/review-form.html"
    form_class = ReviewForm
    success_url = reverse_lazy("reviews:thanks")
    #
    #
    def form_valid(self, form):
        data = form.cleaned_data
        user = self.request.user if self.request.user.is_authenticated else None
        if (user):  
            username = user.username  
        else:
            username = data.get("username", "").strip() or "Unregistered User"
        data["username"] = username
        ## Set up email to send
        to = "cunningham.heatherirene@gmail.com"
        subject = "Review submitted"
        content = f'''<p>Hey Admin or PR Manager!</p>
            <p>Play2Learn feedback received:</p>
            <p>Please, login to the admin site if you wish to mark this review as featured 
            and display it on the home page.</p>  
            <p>Only featured reviews will display on the home page.</p>
            <ul>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>' 
        content += '</ul>'
        send_email(to, subject, content)
        # Save the review with the updated username||"Unregistered User"
        #  and user||Null 
        form.instance.user = user
        form.instance.username = username
        form.instance.save()
        return super().form_valid(form)
## END class ReviewFormView


class ReviewThanksView(TemplateView):
    template_name = "reviews/thanks.html"
## END class ReviewThanksView