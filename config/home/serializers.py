from .models import Project, Task
from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from accounts.serializers import UserSerializer
from accounts.models import User



class ProjectSerializers(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     source='owner'

    # )

    # members = serializers.ManyRelatedField(
    #     queryset=User.objects.all(),
    #     many=True
    # )

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'owner', 'members' ]
        