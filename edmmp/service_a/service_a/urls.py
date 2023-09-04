from django.contrib import admin
from django.urls import path, include
from app_a.urls import urlpatterns as app_a_urls

urlpatterns = [
    path("app_a/", include(app_a_urls)),
    path("admin/", admin.site.urls),
]
