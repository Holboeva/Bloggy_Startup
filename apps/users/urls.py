from django.urls import path

from .views import MeView, RegisterView, UserDetailView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", MeView.as_view(), name="me"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]

