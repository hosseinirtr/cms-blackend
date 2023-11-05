from .models import Post
from .serializers import PostSerializers
from rest_framework import viewsets


from rest_framework.authentication import SessionAuthentication
from blogDjnago.utils import IsAuthenticatedForPostOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedForPostOnly]
