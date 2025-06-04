from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = UserAdmin.list_display + ("is_active", "is_superuser", "birthdate", "joined", "avatar",) 
    list_display_links = ("username", "first_name", "last_name", "email", )
    list_filter = ("is_staff", "is_superuser", "is_active", "birthdate", "joined",)
    search_fields = ("first_name", "last_name", "email", "username",)
    #
    #
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
        return queryset
    deactivate_users.short_description = "Deactivate selected users"
    #
    #
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )
## END CustomUser model Class


## Unregistering default apps not used from `django-allauth`:
admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)