from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    ## Admin app
    path("admin/", admin.site.urls),

    ## Auth, Accounts, & User Management
    path("account/", include("users.urls")),
    path("account/", include("allauth.urls")),

    ## My Local Apps
    path("", include("games.urls")),
    path("", include("pages.urls")),
    path("", include("reviews.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
