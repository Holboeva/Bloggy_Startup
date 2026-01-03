from rest_framework.generics import RetrieveUpdateAPIView
from .models import User
from .serializers import UserProfileSerializer

class ProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "username"
