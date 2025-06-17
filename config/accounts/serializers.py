from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     style={
                                         'input_type':'password',
                                     })
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_staff'] 


    def create(self, validated_data):

        user = User.objects.create_user(
            name = validated_data.get('name', ''),
            email = validated_data['email'],
            password = validated_data['password']

        )

        return user
    
    # accounts/serializers.py -> UserSerializer

    # نسخه صحیح و مقاوم
    def update(self, instance, validated_data):
        # رمز عبور را جدا می‌کنیم تا به صورت خاص آن را مدیریت کنیم
        password = validated_data.pop('password', None)

        # ۱. فیلدهای عادی (مثل name و email) را به متد update کلاس والد می‌سپاریم
        # این متد به صورت استاندارد فیلدها را آپدیت کرده و instance.save() را فراخوانی می‌کند
        instance = super().update(instance, validated_data)

        # ۲. اگر رمز عبور جدیدی ارسال شده بود، آن را هش کرده و دوباره ذخیره می‌کنیم
        if password:
            instance.set_password(password)
            instance.save()

        return instance
    
# افزودن اطلاعات کاربر برای تعیین دسترسی 
class MyTokenObtainPairSerializerWithUserData(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializer(self.user)
        data['user'] = serializer.data

        return data