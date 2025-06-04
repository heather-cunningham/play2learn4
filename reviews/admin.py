from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review 
    list_display = ["first_name", "last_name", "email", "username",  "user", "comments",
                     "review_date_time", "is_featured"]
    list_filter = ("first_name", "last_name", "email", "username", "review_date_time", "is_featured")
    search_fields = ("first_name", "last_name", "email", "username", "comments")
    actions = ["mark_featured", "remove_featured"]
    #
    #
    def mark_featured(self, request, queryset):
        queryset.update(is_featured=True)
        return queryset
    mark_featured.short_description = "Mark selected reviews as featured"
    #
    #
    def remove_featured(self, request, queryset):
        queryset.update(is_featured=False)
        return queryset
    remove_featured.short_description = "Remove featured status from selected reviews"
    #
    #
    def get_readonly_fields(self, request, obj=None):
        if(obj):
            return ("first_name", "last_name", "comments", "review_date_time")
        return ()

