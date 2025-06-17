from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'manager', views.UsersManager, basename='manager')

app_name = 'accounts'
urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/set_password', views.SetPasswordView.as_view(), name='set_password'),
    
]
