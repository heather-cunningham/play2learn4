from django.contrib import admin
from pages.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ["first_name", "last_name", "email", "username", "comments", "contact_date_time"]
    list_display_links = ("first_name", "last_name", "username", "email", "username", "comments",)
    list_filter = ("contact_date_time",)
    search_fields = ("first_name", "last_name", "email", "username", "comments",)
    #
    #
    def get_readonly_fields(self, request, obj=None):
        if(obj):
            return ("first_name", "last_name", "comments", "contact_date_time")
        return ()
