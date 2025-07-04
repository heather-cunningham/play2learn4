import html
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView
from common.utils.email import send_email
from pages.forms import ContactUsForm
from reviews.models import Review


class HomePageView(ListView):
    model = Review
    template_name = "pages/home.html"
    context_object_name = "reviews"
    #
    #
    def get_queryset(self):
        """ Return featured reviews for the homepage carousel. """
        queryset = Review.objects.filter(is_featured=True).order_by("-review_date_time")
        if not queryset.exists():
            return []
        return queryset


class AboutUsView(TemplateView):
    template_name = "pages/about.html"


class ContactUsFormView(FormView):
    template_name = "pages/contact-us.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("pages:contact-thanks")
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
        subject = "'Contact Us' form submitted"
        content = f'''<p>Hello Customer Service,</p>
            <p>A contact or question has been received:</p>
            <ul>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>' 
        content += '</ul>'
        send_email(to, subject, content)
        # Save the review with the updated username/"Unregistered User"
        #  and user/Null 
        form.instance.user = user
        form.instance.username = username
        form.instance.save()
        return super().form_valid(form)
## END class ContactUsFormView


class ContactUsThanksView(TemplateView):
    template_name = "pages/contact-thanks.html"
## END class ContactUsThanksView

