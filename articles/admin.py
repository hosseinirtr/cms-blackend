from django.contrib import admin
from .models import Post, Tag
from .views import PostViewSet, TagViewSet


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    pass  # You can customize this if needed


class TagAdmin(admin.ModelAdmin):
    pass  # You can customize this if needed


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
