from django.contrib import admin
from pages.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ["first_name", "last_name", "email", "username",  "user", "comments",
                     "contact_date_time"]
    #
    #
    def get_readonly_fields(self, request, obj=None):
        if(obj):
            return ("first_name", "last_name", "comments", "contact_date_time")
        return ()
