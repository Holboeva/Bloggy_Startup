from django.urls import path

from apps.views import hello_api_view

urlpatterns = [
    path('', hello_api_view)
]