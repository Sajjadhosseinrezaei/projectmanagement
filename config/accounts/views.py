from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrAdmin
# Create your views here.

User = get_user_model()

class UsersManager(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        تعیین سظح دسترسی بر اساس نوع درخواست 
        """

        # به ثبت نام همه دسترسی دارند
        if self.action == 'create':
            permission_classes = [AllowAny,]
        
        # فقط ادمین ها به لیست کاربران دسترسی دارند
        elif self.action == 'list':
            permission_classes = [IsAdminUser,]

        # برای بقیه اکشن ها کاربر باید لاگین کرده باشد و صاحب پروفایل یا ادمین باشد
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


        return [permission() for permission in permission_classes]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]






class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    


class SetPasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not user.check_password(old_password):
            return Response({'old_password': ['رمز عبور فعلی اشتباه است.']}, status=status.HTTP_400_BAD_REQUEST)

        # میتوانید validation های بیشتری برای رمز جدید اضافه کنید
        user.set_password(new_password)
        user.save()
        return Response({'message': 'رمز عبور با موفقیت تغییر کرد.'}, status=status.HTTP_200_OK)