from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("delete", views.add, name="add")
]