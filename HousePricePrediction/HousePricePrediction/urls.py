from django.contrib import admin
from django.urls import include, path
from django.urls import path
from django.conf import settings

urlpatterns = [
    path("", include("prediction.urls")),
    path("admin/", admin.site.urls),
]
