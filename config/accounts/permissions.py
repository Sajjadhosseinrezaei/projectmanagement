from rest_framework import permissions



class IsOwnerOrAdmin(permissions.BasePermission):
    """
    کلاس دسترسی سفارشی که فقط به صاحب آبجکت یا ادمین ها اجازه دسترسی میدهد
    """
    def has_object_permission(self, request, view, obj):
        # ادمین ها به همه چیز دسترسی دارند
        if request.user.is_staff:
            return True
        # فقط صاحب پروفایل دسترسی به ابجکت دارد 
        # obj نمونه ای است که کاربر اطلاعاتش قرار است تغییر کند
        return obj == request.user

        return super().has_object_permission(request, view, obj)