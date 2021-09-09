from django.urls import path
from .views import AuthURl, spotify_callback

urlpatterns = [
    path('/get-auth-url', AuthURl.as_view()),
    path('redirect', spotify_callback)
]
