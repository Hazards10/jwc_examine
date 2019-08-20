# -*- coding: utf-8 -*-
from django.db import models

from datetime import datetime  #引入datatime包，获取系统时间
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
    date = models.CharField(max_length=50, verbose_name="日期")
    term = models.CharField(max_length=50, verbose_name="学期" )
    data_name = models.CharField(max_length=50, verbose_name="设备名称")
    data_company = models.CharField(max_length=50, verbose_name="单位" )
    data_count = models.CharField(max_length=50, verbose_name="数量")
    data_price = models.CharField(max_length=50, verbose_name="预算单价")
    data_price2 = models.CharField(max_length=50, verbose_name="预算金额")
    data_company2 = models.CharField(max_length=50, verbose_name="使用单位")
    data_parameter = models.CharField(max_length=50, verbose_name="规格及技术参数")
    creator = models.CharField(max_length=50, verbose_name="创建者")
    examine = models.CharField(max_length=50, verbose_name="一级审核者")
    admin = models.CharField(max_length=50, verbose_name="二级审核者")
    check_1 = models.BooleanField(default=False, verbose_name="学院审核")
    check_2 = models.BooleanField(default=False, verbose_name="教务处审核")
    is_buy = models.BooleanField(default=False, verbose_name="仪器是否购买")
    is_deposit = models.BooleanField(default=False, verbose_name="仪器是否入库")


class CheckFormHC(models.Model):
    """耗材表"""
    data_id = models.AutoField(primary_key=True, verbose_name="编号")
    date = models.CharField(max_length=50, verbose_name="创建时间")
    term = models.CharField(max_length=50, verbose_name="学期")
    data_name = models.CharField(max_length=50, verbose_name="材料名称")
    data_parameter = models.CharField(max_length=50, verbose_name="材料规格")
    data_company = models.CharField(max_length=50, verbose_name="单位")
    data_count = models.CharField(max_length=50, verbose_name="数量")
    data_price = models.CharField(max_length=50, verbose_name="单价")
    data_price2 = models.CharField(max_length=50, verbose_name="金额")
    data_usedate = models.CharField(max_length=50, verbose_name="使用日期")
    data_person = models.CharField(max_length=50, verbose_name="验收领用人")
    data_remark = models.CharField(max_length=50, verbose_name="备注", null=True, blank=True)
    creator = models.CharField(max_length=50, verbose_name="创建者")
    examine = models.CharField(max_length=50, verbose_name="一级审核者")
    admin = models.CharField(max_length=50, verbose_name="二级审核者")
    check_1 = models.BooleanField(default=False, verbose_name="学院审核")
    check_2 = models.BooleanField(default=False, verbose_name="教务处审核")
    is_buy = models.BooleanField(default=False, verbose_name="耗材是否购买")
    is_deposit = models.BooleanField(default=False, verbose_name="耗材是否入库")


class AdminForm(models.Model):
    """用户表"""
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50, verbose_name="教室姓名")
    admin_teacherNo = models.CharField(max_length=50, verbose_name="工号")
    admin_rank = models.CharField(max_length =20, verbose_name="用户等级")# 三个等级，学院老师，学院领导，教务处老师，等级依次递增
    admin_unit = models.CharField(max_length=20, verbose_name="工作单位")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="账号添加时间")
