from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class MeView(APIView):
    """
    Authenticated user's own profile.

    - GET    /api/users/me/      → retrieve current profile
    - PATCH  /api/users/me/      → partial update (first_name, last_name, bio, skills, ...)
    - DELETE /api/users/me/      → delete account
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailView(generics.RetrieveAPIView):
    """
    Read‑only endpoint to view another user's public profile.

    - GET /api/users/<id>/
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
