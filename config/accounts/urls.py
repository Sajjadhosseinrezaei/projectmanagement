from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('list/', views.ListUsers.as_view(), name='list'),
]
