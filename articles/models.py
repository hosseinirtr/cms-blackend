from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tag(models.Model):
    slug = models.CharField(max_length=62)
    title = models.CharField(max_length=144)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    LOCALE_CHOICES = [
        ("Farsi", "FARSI"),
        ("English", "ENGLISH"),
        ("Italian", "ITALIAN"),
    ]
    title = models.CharField(max_length=144)
    content = models.TextField()
    slug = models.CharField(max_length=62)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    locale = models.CharField(max_length=20, choices=LOCALE_CHOICES, default="FARSI")

    og_description = models.TextField(max_length=164)

    image = models.ImageField(
        upload_to="post_images/", null=True
    )  # Use ImageField for images

    def __str__(self) -> str:
        return f"{self.title} at {self.created_at}"
