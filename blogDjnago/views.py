from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView

# Create your views here.
    
class SuperuserAuthView(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request,user)
            return JsonResponse({"msg":"Super user found"}, status=status.HTTP_200_OK) 
        else:
            return JsonResponse({"error": "Invalid credentials or not a superuser."}, status=status.HTTP_401_UNAUTHORIZED)

