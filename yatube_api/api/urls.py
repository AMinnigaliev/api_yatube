from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet, basename='group')
router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
