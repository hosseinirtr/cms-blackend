from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Post
from .serializers import PostSerializers
from rest_framework import viewsets, status
from rest_framework.views import APIView


from rest_framework.decorators import authentication_classes, permission_classes, action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from blogDjnago.utils import IsAuthenticatedForPostOnly

class PostViewSet(viewsets.ModelViewSet):    
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedForPostOnly]