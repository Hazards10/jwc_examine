# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Log(models.Model):
    """
    日志表
    """
    id = models.AutoField(primary_key=True)
    A = models.CharField(max_length=50)
    B = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    type = models.IntegerField()


class CheckFormYQ(models.Model):
    """
    仪器表
    """
    data_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=20, verbose_name="日期")
    term = models.CharField(max_length=20, verbose_name="学期" )
    data_name = models.CharField(max_length=50, verbose_name="设备名称")
    data_company = models.CharField(max_length=10, verbose_name="单位" )
    data_count = models.CharField(max_length=10, verbose_name="数量")
    data_price = models.CharField(max_length=10, verbose_name="预算单价")
    data_price2 = models.CharField(max_length=10, verbose_name="预算金额")
    data_company2 = models.CharField(max_length=10, verbose_name="使用单位")
    data_parameter = models.TextField(verbose_name="规格及技术参数")
    creator = models.CharField(max_length=10, verbose_name="创建者")
    examine = models.CharField(max_length=10, verbose_name="一级审核者")
    admin = models.CharField(max_length=10, verbose_name="二级审核者")
    check_1 = models.BooleanField(default=False, verbose_name="学院审核")
    check_2 = models.BooleanField(default=False, verbose_name="教务处审核")
    is_buy = models.BooleanField(default=False, verbose_name="仪器是否购买")
    is_deposit = models.BooleanField(default=False, verbose_name="仪器是否入库")


class CheckFormHC(models.Model):
    """耗材表"""
    data_id = models.AutoField(primary_key=True, verbose_name="编号")
    date = models.CharField(max_length=20, verbose_name="创建时间")
    term = models.CharField(max_length=10, verbose_name="学期")
    data_name = models.CharField(max_length=50, verbose_name="材料名称")
    data_parameter = models.CharField(max_length=50, verbose_name="材料规格")
    data_company = models.CharField(max_length=10, verbose_name="单位")
    data_count = models.CharField(max_length=10, verbose_name="数量")
    data_price = models.CharField(max_length=10, verbose_name="单价")
    data_price2 = models.CharField(max_length=10, verbose_name="金额")
    data_usedate = models.CharField(max_length=20, verbose_name="使用日期")
    data_person = models.CharField(max_length=10, verbose_name="验收领用人")
    data_remark = models.CharField(max_length=50, verbose_name="备注", null=True, blank=True)
    course_name = models.CharField(max_length=20, verbose_name="所属课程名称", default="")
    experiment_name = models.CharField(max_length=20, verbose_name= "实验课程名称",default="")
    class_name = models.CharField(max_length=20, verbose_name="实验班级名称",default="")
    experiment_number = models.CharField(max_length=20, verbose_name="实验人数", default="")
    creator = models.CharField(max_length=10, verbose_name="创建者")
    examine = models.CharField(max_length=10, verbose_name="一级审核者")
    admin = models.CharField(max_length=10, verbose_name="二级审核者")
    check_1 = models.BooleanField(default=False, verbose_name="学院审核")
    check_2 = models.BooleanField(default=False, verbose_name="教务处审核")
    is_buy = models.BooleanField(default=False, verbose_name="耗材是否购买")
    is_deposit = models.BooleanField(default=False, verbose_name="耗材是否入库")
