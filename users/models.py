from datetime import datetime

from django.db import models


from django.contrib.auth.models import AbstractUser


RANK_CHOICES = (
    ("普通老师", "普通老师"),
    ("学院领导", "学院领导"),
    ("教务处老师", "教务处老师")
)


class UserProfile(AbstractUser):
    admin_teacherNo = models.CharField(max_length=20, verbose_name="工号", default="")
    admin_rank = models.CharField(max_length=7,choices=RANK_CHOICES, verbose_name="用户等级")  # 三个等级，学院老师，学院领导，教务处老师，等级依次递增
    admin_unit = models.CharField(max_length=20, verbose_name="工作单位")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="账号添加时间")
