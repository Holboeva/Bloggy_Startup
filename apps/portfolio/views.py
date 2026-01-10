from rest_framework import generics, permissions
from .models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioView(generics.RetrieveUpdateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        portfolio, created = Portfolio.objects.get_or_create(user=self.request.user)
        return portfolio
