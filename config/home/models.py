from django.db import models
from accounts.models import User

# تعریف گزینه‌ها برای وضعیت و اولویت
STATUS_CHOICES = [
    ('pending', 'در انتظار'),
    ('in_progress', 'در حال انجام'),
    ('completed', 'تکمیل‌شده'),
]

PRIORITY_CHOICES = [
    ('low', 'کم'),
    ('medium', 'متوسط'),
    ('high', 'زیاد'),
]

class Project(models.Model):
    """
    مدلی برای نمایش یک پروژه.
    این مدل شامل عنوان، توضیحات، تاریخ ایجاد، صاحب پروژه و اعضای پروژه است.
    امکان همکاری چندین کاربر در یک پروژه را فراهم می‌کند.
    """
    title = models.CharField(
        max_length=100,
        help_text="عنوان پروژه با حداکثر ۱۰۰ کاراکتر برای شناسایی آسان"
    )
    description = models.TextField(
        help_text="توضیحات کامل درباره اهداف و جزئیات پروژه"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text="تاریخ و زمان ایجاد پروژه، به صورت خودکار هنگام ساخت تنظیم می‌شود"
    )

    updated = models.DateTimeField(
        auto_now=True,
        help_text="آخرین زمان ویرایش پروژه ، به صورت خودکار ثبت میشود"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects',
        help_text="کاربری که پروژه را ایجاد کرده و صاحب آن است؛ با حذف کاربر، پروژه حذف می‌شود"
    )
    members = models.ManyToManyField(
        User,
        related_name='member_projects',
        help_text="کاربرانی که به عنوان عضو در پروژه مشارکت دارند؛ هر کاربر می‌تواند در چندین پروژه عضو باشد"
    )

    def __str__(self):
        """
        نمایش رشته‌ای مدل پروژه.
        عنوان پروژه را برای شناسایی آسان در ادمین یا جاهای دیگر برمی‌گرداند.
        """
        return self.title

    class Meta:
        ordering = ['created']  # مرتب‌سازی پیش‌فرض پروژه‌ها بر اساس تاریخ ایجاد
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"


class Task(models.Model):
    """
    مدلی برای نمایش یک وظیفه در یک پروژه.
    شامل عنوان، توضیحات، پروژه مرتبط، کاربر اختصاص‌یافته، وضعیت، اولویت و مهلت است.
    برای مدیریت وظایف تیمی و پیگیری پیشرفت استفاده می‌شود.
    """
    title = models.CharField(
        max_length=100,
        help_text="عنوان وظیفه با حداکثر ۱۰۰ کاراکتر برای شناسایی سریع"
    )
    description = models.TextField(
        help_text="توضیحات مفصل درباره کارهایی که باید برای این وظیفه انجام شود"
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
        help_text="پروژه‌ای که این وظیفه به آن تعلق دارد؛ با حذف پروژه، وظیفه حذف می‌شود"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks',
        help_text="کاربری که وظیفه به او اختصاص داده شده؛ می‌تواند خالی باشد و با حذف کاربر، به null تنظیم می‌شود"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="وضعیت کنونی وظیفه: در انتظار، در حال انجام یا تکمیل‌شده"
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium',
        help_text="سطح اولویت وظیفه: کم، متوسط یا زیاد"
    )
    deadline = models.DateTimeField(
        help_text="تاریخ و زمان مهلت برای تکمیل وظیفه"
    )

    def __str__(self):
        """
        نمایش رشته‌ای مدل وظیفه.
        عنوان وظیفه و عنوان پروژه مرتبط را برای شناسایی آسان برمی‌گرداند.
        """
        return f"{self.title} - {self.project.title}"

    class Meta:
        ordering = ['deadline']  # مرتب‌سازی پیش‌فرض وظایف بر اساس مهلت
        verbose_name = "وظیفه"
        verbose_name_plural = "وظایف"