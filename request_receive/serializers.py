from rest_framework import serializers
from .models import TeammateRequest, SponsorRequest


class TeammateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeammateRequest
        fields = "__all__"


class SponsorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorRequest
        fields = "__all__"
