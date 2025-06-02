from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     style={
                                         'input_type':'password',
                                     })
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password'] 


    def create(self, validated_data):

        user = User.objects.create(
            name = validated_data.get('name', ''),
            email = validated_data['email'],
            password = validated_data['password']

        )

        return user
    
    def update(self, instance, validated_data):
        
        password = validated_data.pop('password', None)

        for attr , val in validated_data.items():
            setattr(instance, attr, val)

        if password:
            instance.set_password(password)

        instance.save()

        return instance
