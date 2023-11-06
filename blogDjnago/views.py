from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.models import User

# Create your views here.


class SuperuserAuthViewSet(APIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return JsonResponse({"msg": "Super user found"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(
                {"error": "Invalid credentials or not a superuser."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(user)
            return Response(serializer.data)
