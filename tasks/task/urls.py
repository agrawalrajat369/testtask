from django.urls import path, include
from .views import TestRequest

urlpatterns = [
    path('request/', TestRequest.as_view()),
]