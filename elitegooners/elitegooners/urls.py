
from django.contrib import admin
from django.urls import path
from .views import hello_elites

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hi/', hello_elites)
]
