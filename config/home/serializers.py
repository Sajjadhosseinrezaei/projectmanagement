from .models import Project, Task
from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from accounts.serializers import UserSerializer
from accounts.models import User



class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'owner', 'members' ]

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'
        