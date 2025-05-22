from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review 
    list_display = ["first_name", "last_name", "email", "username",  "user", "comments",
                     "review_date_time"]
    #
    #
    def get_readonly_fields(self, request, obj=None):
        if(obj):
            return ("first_name", "last_name", "comments", "review_date_time")
        return ()

