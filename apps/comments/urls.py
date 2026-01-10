from rest_framework_nested.routers import NestedDefaultRouter
from apps.posts.views import PostViewSet
from .views import CommentViewSet
from apps.posts.urls import router as posts_router

# posts_router = DefaultRouter() ichida PostViewSet bor
router = NestedDefaultRouter(posts_router, "posts", lookup="post")
router.register("comments", CommentViewSet, basename="post-comments")

urlpatterns = router.urls
