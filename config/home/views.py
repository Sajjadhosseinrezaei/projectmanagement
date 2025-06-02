from django.shortcuts import render
from .serializers import ProjectSerializer, TaskSerializer
from .models import Project, Task
from rest_framework import viewsets


# Create your views here.
class ProjectManager(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskManager(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer