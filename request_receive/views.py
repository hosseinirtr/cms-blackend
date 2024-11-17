from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from .models import TeammateRequest, SponsorRequest
from .serializers import (
    TeammateRequestSerializer,
    SponsorRequestSerializer,
)  # Create a serializer for Teammate


class TeammateViewSet(viewsets.ModelViewSet):
    queryset = TeammateRequest.objects.all()
    serializer_class = TeammateRequestSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset  # Authenticated users see all data
        return TeammateRequest.objects.none()  # Unknown users see nothing


class SponsorRequestViewSet(viewsets.ModelViewSet):
    queryset = SponsorRequest.objects.all()
    serializer_class = SponsorRequestSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset  # Authenticated users see all data
        return TeammateRequest.objects.none()  # Unknown users see nothing
