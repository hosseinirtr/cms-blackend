from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles import views
import request_receive


from django.conf import settings
from django.conf.urls.static import static

import request_receive.views

from .views import SuperuserAuthViewSet


router = DefaultRouter()
router.register(
    r"api/posts",
    views.PostViewSet,
)
router.register(
    r"api/tags",
    views.TagViewSet,
)

router.register(r"api/teammate-requests", request_receive.views.TeammateViewSet)
router.register(r"api/sponsor-requests", request_receive.views.SponsorRequestViewSet)

# Tag TagViewSet
# router.register(r"auth", SuperuserAuthViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/auth/superuser/", SuperuserAuthViewSet.as_view(), name="superuser-auth"),
    path("api/posts", views.PostViewSet.as_view({"get": "list"}), name="Post"),
    path("api/tags", views.TagViewSet.as_view({"get": "list"}), name="tag"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
