from django.contrib import admin
from django.urls import path
from . import views

app_name = "articles"

# from django.apps import apps


# models = apps.get_models()

# for model in models:
#     admin.site.register(model)

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("delete", views.add, name="add"),
]
