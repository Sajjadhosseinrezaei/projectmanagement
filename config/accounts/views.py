from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# Create your views here.

User = get_user_model()

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer