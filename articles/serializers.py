from rest_framework import serializers

from .models import Post, Tag


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "slug",
            "title",
            "parent",
        ]


class PostSerializers(serializers.ModelSerializer):
    tags = TagSerializers(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "slug", "tags", "created_at", "image", "og_description", ]
