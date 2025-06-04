from django.shortcuts import render
from .serializers import DashboardSerializer, TaskSerializer, ProjectSerializer
from .models import Project, Task
from rest_framework import viewsets
from .filters import TaskFilter
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ProjectManager(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskManager(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = TaskFilter



class DashboardView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = DashboardSerializer(instance={}, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
