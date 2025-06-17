from .models import Project, Task
from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from accounts.serializers import UserSerializer
from accounts.models import User



class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'owner', 'members' ]
        read_only_fields = ['owner',]

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'


class DashboardSerializer(serializers.Serializer):
    completed_tasks = serializers.SerializerMethodField()
    pending_tasks = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()



    def get_completed_tasks(self, obj):
        return Task.objects.filter(status='completed').count()

    def get_pending_tasks(self, obj):
        return Task.objects.filter(status='pending').count()
    

    def get_projects(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            projects = Project.objects.filter(owner=request.user)
            if projects.exists():
                return ProjectSerializer(projects, many=True).data
        return None


