from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.urls import re_path as url
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.PostViewSet, name="index"),
    path("add", views.PostViewSet, name="add"),
    path("delete", views.PostViewSet, name="add"),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
