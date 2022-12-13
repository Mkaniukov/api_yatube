from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import GroupViewSet, PostViewSet, CommentViewSet


router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
    ]
