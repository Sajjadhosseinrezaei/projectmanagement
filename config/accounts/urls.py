from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'manager', views.UsersManager, basename='manager')

app_name = 'accounts'
urlpatterns = [
    path('', include(router.urls)),
]
