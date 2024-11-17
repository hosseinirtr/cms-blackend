from django.urls import path
from . import views

urlpatterns = [
    path('teammates/', views.teammate_list, name='teammate_list'),
    path('teammates/<int:pk>/', views.teammate_detail, name='teammate_detail'),
    path('teammates/new/', views.teammate_create, name='teammate_create'),
    
    path('sponsor-requests/', views.sponsor_request_list, name='sponsor_request_list'),
    path('sponsor-requests/new/', views.sponsor_request_create, name='sponsor_request_create'),
]
