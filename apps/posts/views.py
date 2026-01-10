from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            return Response({"liked": False})
        else:
            post.likes.add(user)
            return Response({"liked": True})

    @action(detail=False, methods=["get"])
    def stats(self, request):
        return Response({
            "total_posts": Post.objects.count(),
            "total_likes": sum(p.likes.count() for p in Post.objects.all())
        })

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

