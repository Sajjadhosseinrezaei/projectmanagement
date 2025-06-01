from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    # متد برای ایجاد کاربر معمولی
    def create_user(self, email, name='', password=None, **extra_fields):
        """
        ایجاد و ذخیره یک کاربر معمولی با ایمیل، نام و رمز عبور
        """
        if not email:
            raise ValueError('ایمیل باید وارد شود')


        # نرمال‌سازی ایمیل (تبدیل به فرمت استاندارد)
        email = self.normalize_email(email)
        # ایجاد نمونه کاربر
        user = self.model(email=email, name=name, **extra_fields)
        # تنظیم رمز عبور
        user.set_password(password)
        user.save(using=self._db)
        return user

    # متد برای ایجاد سوپریوزر (ادمین)
    def create_superuser(self, email, name='', password=None, **extra_fields):
        """
        ایجاد و ذخیره یک سوپریوزر با ایمیل، نام و رمز عبور
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
   

        if extra_fields.get('is_staff') is not True:
            raise ValueError('سوپریوزر باید is_staff=True باشد')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('سوپریوزر باید is_superuser=True باشد')

        return self.create_user(email, name, password, **extra_fields)