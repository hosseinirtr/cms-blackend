from rest_framework import serializers
from .models import Post, Tag


class PostSerializers(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), allow_empty=True
    )

    class Meta:
        model = Post
        fields = ["id", "title", "content", "slug", "tags", "created_at", "image"]


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "slug",
            "title",
            "parent",
        ]
