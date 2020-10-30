from django.urls import path, include
from .views import ProfileDetail

urlpatterns = [
    path('', ProfileDetail.as_view()),
]
