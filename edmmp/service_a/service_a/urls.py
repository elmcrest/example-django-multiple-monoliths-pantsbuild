from app_a.urls import urlpatterns as app_a_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("app_a/", include(app_a_urls)),
    path("admin/", admin.site.urls),
]
