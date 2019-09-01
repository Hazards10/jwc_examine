"""Jwc_examine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from Jwc_examine.settings import MEDIA_ROOT
from main_app import views_router, views_add, views_commit, views_get, views_login, views_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root':MEDIA_ROOT}),   # 文件映射路径
    # 路由地址
    path('', views_router.page_login),  # 登陆界面
    path('index/', views_router.home),  # 首页
    path('request_list/', views_router.apply_list),  # 请求列表
    # HC
    path('add_hc_view/', views_router.add_hc_view),  # 创建hc
    path('examine_hc1_view/', views_router.examine_hc_1_view),  # 一级审核(全部)
    path('examine_hc1_single_view/', views_router.examine_hc_1_single_view),  # 一级审核(single)
    path('examine_hc2_view/', views_router.examine_hc_2_view),  # 二级审核(全部)
    path('examine_hc2_view_buy/', views_router.examine_hc2_view_buy), #二级审核购买标记
    path('examine_hc2_view_deposit/', views_router.examine_hc2_view_deposit), #二级审核入库标记
    path('examine_hc2_single_view/', views_router.examine_hc_2_single_view),  # 二级审核(single)
    path('show_hc_creator/', views_router.show_hc_creator),  # 显示创建者耗材提交的结果(single)
    path('show_hc_examine/', views_router.show_hc_examine),  # 显示审核者的学院审核结果(single)
    path('show_hc_admin/', views_router.show_hc_admin),  # 显示教务处审核结果(全部)
    path('show_hc_admin_buy/', views_router.show_hc_admin_buy),  # 显示教务处审核购买标记的结果(全部)
    path('show_hc_admin_deposit/', views_router.show_hc_admin_deposit), #显示教务处审核入库标价结果（全部）
    # YQ
    path('add_yq_view/', views_router.add_yq_view),  # 创建yq
    path('examine_yq1_view/', views_router.examine_yq_1_view),  # 一级审核(全部)
    path('examine_yq1_single_view/', views_router.examine_yq_1_single_view),  # 一级审核(single)
    path('examine_yq2_view/', views_router.examine_yq_2_view),  # 二级审核(全部)
    path('examine_yq2_single_view/', views_router.examine_yq_2_single_view),  # 二级审核(single)
    path('examine_yq2_view_buy/', views_router.examine_yq2_view_buy), #二级审核购买标记
    path('examine_yq2_view_deposit/', views_router.examine_yq2_view_deposit), #二级审核入库标记
    path('show_yq_creator/', views_router.show_yq_creator),  # 显示创建者仪器提交的结果(single)
    path('show_yq_examine/', views_router.show_yq_examine),  # 显示通过二级审核(single)
    path('show_yq_admin/', views_router.show_yq_admin),  # 显示教务处审核结果(全部)
    path('show_yq_admin_buy/', views_router.show_yq_admin_buy),  #显示教务处审核购买结果（全部）
    path('show_yq_admin_deposit/', views_router.show_yq_admin_deposit),  #显示教务处审核入库结果（结果）

    # 操作地址
    path('login/', views_login.login),  # 登陆验证
    path('get_request_list/', views_get.get_sender),  # 得到请求列表
    path('add_hc/', views_add.add_hc),  # 创建hc
    path('add_yq/', views_add.add_yq),  # 创建yq
    path('del_hc/', views_delete.del_hc),  # 删除hc
    path('del_yq/', views_delete.del_yq),  # 删除yq
    path('edit_hc_creator/', views_get.GetEditHcCreator.as_view()),  # 获取或编辑一条hc数据(普通老师)
    path('edit_yq_creator/', views_get.GetEditYqCreator.as_view()),  # 获取或编辑一条hc数据(普通老师)
    path('excel_add_hc/', views_add.excel_commit_hc),  # excel导入耗材数据
    path('excel_add_yq/', views_add.excel_commit_yq),  # excel导入仪器数据
    path('add_admin/', views_add.add_admin),    #创建用户
    path('edit_admin/', views_add.edit_admin),    #创建用户
    # HC
    path('get_examine_list_hc/', views_get.get_examine_list_hc),  # 得到一级审核表
    path('get_second_examine_list_hc/', views_get.get_second_examine_list_hc),  # 得到二级审核表
    path('get_second_examine_buy_list_hc/', views_get.get_second_examine_buy_list_hc), #得到二级购买审核列表
    path('get_second_examine_deposit_list_hc/', views_get.get_second_examine_deposit_list_hc), #得到二级入库审核列表
    path('get_examine_single_list_hc/', views_get.get_examine_single_list_hc),  # 得到一级审核表(single)
    path('get_final_single_list_hc/', views_get.get_final_single_list_hc),  # 得到二级审核表(single)
    path('commit_check1_hc/', views_commit.commit_check1_hc),  # 一级审核
    path('commit_check2_hc/', views_commit.commit_check2_hc),  # 二级审核
    path('commit_check2_hc_buy/', views_commit.commit_check2_hc_buy),   #二级审核购买标记
    path('commit_check2_hc_deposit/', views_commit.commit_check2_hc_deposit),   #二级审核入库标记
    path('show_check_hc_creator/', views_get.show_check_hc_creator),  # 显示通过学院老师提交过的结果 creator
    path('show_check_hc_examine/', views_get.show_check_hc_examine),  # 显示通过学院领导审核过的结果 examine
    path('show_check_all_hc/', views_get.show_check_all_hc),  # 显示所有通过审核    admin
    path('show_check_all_hc_buy/', views_get.show_check_all_hc_buy),  # 显示通过学院领导审核过的购买结果 admin
    path('show_check_all_hc_deposit/', views_get.show_check_all_hc_deposit),  # 显示通过学院领导审核过的入库结果 admin
    # YQ
    path('get_examine_list_yq/', views_get.get_examine_list_yq),  # 得到一级审核表
    path('get_final_list_yq/', views_get.get_final_list_yq),  # 得到二级审核表
    path('get_examine_single_list_yq/', views_get.get_examine_single_list_yq),  # 得到一级审核表(single)
    path('get_second_examine_buy_list_yq/', views_get.get_second_examine_buy_list_yq), #得到二级购买审核列表
    path('get_second_examine_deposit_list_yq/', views_get.get_second_examine_deposit_list_yq), #得到二级入库审核列表
    path('get_final_single_list_yq/', views_get.get_final_single_list_yq),  # 得到二级审核表(single)
    path('commit_check1_yq/', views_commit.commit_check1_yq),  # 一级审核
    path('commit_check2_yq/', views_commit.commit_check2_yq),  # 二级审核
    path('commit_check2_yq_buy/', views_commit.commit_check2_yq_buy),   #二级审核购买标记
    path('commit_check2_yq_deposit/', views_commit.commit_check2_yq_deposit),   #二级审核入库标记
    path('show_check_yq_creator/', views_get.show_check_yq_creator),  # 显示通过学院老师提交过的结果 creator
    path('show_check_yq_examine/', views_get.show_check_yq_examine),  # 显示通过学院领导审核过的结果 examine
    path('show_check_all_yq/', views_get.show_check_all_yq),  # 显示所有通过审核    admin
    path('show_check_all_yq_buy/', views_get.show_check_all_yq_buy),  # 显示通过学院领导审核过的购买结果 admin
    path('show_check_all_yq_deposit/', views_get.show_check_all_yq_deposit),  # 显示通过学院领导审核过的入库结果 admin

    # 用户管理
    path('show_admin/', views_router.show_admin_view),   # 显示用户
    path('get_admin_all/',views_get.show_all_admin),    # 获取用户数据接口
    path('add_admin_router/', views_router.add_admin_view),    # 跳转添加用户界面
    path('get_admin_detail/', views_get.get_teacher_info),  # ajax 获取教师详细信息
    path('delete_admin/', views_add.del_admin),     # 删除用户

    # 耗材、仪器ajax获取接口
    path('get_examine/', views_get.get_examine),  # 获取耗材表单提交的下级审核人数据

]
