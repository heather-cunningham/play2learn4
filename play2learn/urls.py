from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ## Admin app
    path("admin/", admin.site.urls),

    ## My Local Apps
    path("", include("games.urls")),
    path("", include("pages.urls")),
    path("", include("reviews.urls")),
]
