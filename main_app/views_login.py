from django.shortcuts import render
from django.views.generic.base import View  # django视图，继承后重载get、post方法
from django.contrib.auth import authenticate, login, logout  # 自带的权限认证函数
from django.http import JsonResponse, HttpResponseRedirect  # json返回响应，重定向响应


from main_app import models



def login(request):
    """
    用户登录验证
    :param request: 
    :return: 用户权限等级或者用户登录失败标志
    """
    if request.is_ajax():
        #获取用户姓名和密码
        admin_name = request.POST.get('admin_name')
        password = request.POST.get('password')
        result = models.AdminForm.objects.filter(admin_name=admin_name, admin_teacherNo = password)
        #如果查询有结果，根据权限返回权限等级
        if result.count()!=0:
            admin_rank = result.values()[0]['admin_rank']
            if admin_rank=='普通老师':
                result = "admin1"
            elif admin_rank=='学院领导':
                result = "admin2"
            elif admin_rank=='教务处老师':
                result = "admin3"
        #查询不到结果，返回false
        else:
              result = "false"
        return JsonResponse(result, safe=False)
