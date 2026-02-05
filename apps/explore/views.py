from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.groups.models import Group
from apps.groups.serializers import GroupSerializer
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from apps.users.models import User
from apps.users.serializers import UserSerializer


class ExploreView(APIView):
    """
    Aggregated explore endpoint used by the Explore page.

    Returns:
    - featured_users: recently joined users
    - trending_posts: posts ordered by like count
    - groups: groups ordered by member count
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        featured_users = User.objects.order_by("-date_joined")[:10]

        trending_posts = (
            Post.objects.annotate(num_likes=Count("likes"))
            .order_by("-num_likes", "-created_at")[:10]
        )

        popular_groups = (
            Group.objects.annotate(num_members=Count("members"))
            .order_by("-num_members", "-created_at")[:10]
        )

        data = {
            "featured_users": UserSerializer(featured_users, many=True).data,
            "trending_posts": PostSerializer(trending_posts, many=True).data,
            "groups": GroupSerializer(popular_groups, many=True).data,
        }
        return Response(data)

