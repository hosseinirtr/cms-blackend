from django.db import models
from django.contrib.postgres.fields import ArrayField

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
    title = models.CharField(max_length=144)
    content = models.TextField()
    slug = models.CharField(max_length=62)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateField(auto_now_add=True)
    is_fa = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="post_images/", null=True
    )  # Use ImageField for images

    def __str__(self) -> str:
        return f"{self.title} at {self.date}"
