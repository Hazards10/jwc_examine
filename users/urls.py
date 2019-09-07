# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/9/6  23:17'

from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('add_admin/', views.add_admin, name="add_admin"),    # 创建用户
    path('edit_admin/', views.edit_admin,name="edit_admin"),    # 创建用户
    path('show_admin/', views.show_admin_view, name="show_admin"),  # 显示用户
    path('get_admin_all/', views.show_all_admin, name="show_all_admin"),    # 获取用户数据接口
    path('get_admin_detail/', views.get_teacher_info, name="get_teacher_info"),  # ajax 获取教师详细信息
    path('delete_admin/', views.del_admin, name="del_admin"),     # 删除用户
    path('get_examine/', views.get_examine, name="get_examine"),  # 耗材、仪器ajax获取接口 获取耗材表单提交的下级审核人数据
]