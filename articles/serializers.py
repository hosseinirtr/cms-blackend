from rest_framework import serializers

from .models import Post, Tag


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostSerializers(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )  # Use PrimaryKeyRelatedField for Many-to-Many field
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = "__all__"
