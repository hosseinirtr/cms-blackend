from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
from rest_framework import viewsets
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializers