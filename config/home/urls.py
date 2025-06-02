from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views




router = DefaultRouter()
router.register(r'project-manager', views.ProjectManager, basename='project-manager')
router.register(r'task-manager', views.TaskManager, basename='task-manager')


app_name = 'home'
urlpatterns = [
    path('', include(router.urls))
    
]
