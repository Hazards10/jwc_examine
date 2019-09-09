import json

from django.urls import reverse  # 用于访问特定的html文件
from django.shortcuts import render
from django.views.generic.base import View  # django视图，继承后重载get、post方法
from django.contrib.auth import authenticate, login, logout  # 自带的权限认证函数
from django.http import JsonResponse, HttpResponseRedirect  # json返回响应，重定向响应
from django.contrib.auth.hashers import make_password

from users.models import UserProfile  # 引入扩展的自定义用户表
from users.forms import LoginForm  # 引入自定义表单验证类
from utils.model_to_dic import model_to_dic
from utils.execute_sql import execute_sql_11
from utils.date_tool import get_term


# 登录接口
class LoginView(View):
    """
    登录视图
    """
    def get(self, request, *args, **kwargs):
        # 判断用户是否登录
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))  # 跳转url地址 返回图片验证码
        # login_form = DynamicLoginForm()
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        # django表单验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=user_name,  password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse('index')) #  跳转url地址
                # django cookies存中文会报错，用json模块处理
                response.set_cookie("user", json.dumps(user.username), max_age=60 * 60 * 60* 24 * 7)  # cookie一周过期
                response.set_cookie("rank", json.dumps(user.admin_rank), max_age=60 * 60 * 60* 24 * 7)
                return response
            else:
                return render(request, 'login.html', {
                    'msg': "用户名或密码错误",
                    'login_form': login_form
                })
        else:
            return render(request, 'login.html', {'login_form': login_form})


# 退出登录
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


# 创建admin用户
def add_admin(request):
    result_data = {"message": False, "note": "用户添加失败！"}
    if request.method == 'POST':
        number = request.POST.get('number')  # 工号
        name = request.POST.get('name')  # 姓名
        unit = request.POST.get('unit')  # 单位
        rank = request.POST.get('rank')  # 用户等级
        data = UserProfile.objects.filter(admin_teacherNo=number)
        # 判断用户是否已经添加过
        if data:
            result_data["message"] = False
            result_data["note"] = "用户已经存在！"
        # 没有添加过，创建用户
        else:
            if UserProfile.objects.create(username=name, admin_teacherNo=number, admin_rank=rank, admin_unit=unit,
                                          password=make_password(number)):
                result_data["message"] = True
                result_data["note"] = "添加用户成功！"
    return JsonResponse(data=result_data, safe=False)


# 修改admin用戶
def edit_admin(request):
    data = {}
    if request.is_ajax():
        admin_id = request.POST.get('edit_adminId')  # 工号
        rank = request.POST.get('rank')     # 用户等级
        if UserProfile.objects.filter(id=admin_id).update(admin_rank=rank):
            data["message"] = True
    return JsonResponse(data=data, safe=False)


# 用户管理
def show_admin_view(request):
    return  render(request, 'show/show_admin.html')


# 显示所有用户信息
def show_all_admin(request):
    if request.method == 'GET':
        data_info = UserProfile.objects.all()
        return JsonResponse(model_to_dic(data_info), safe=False)


# ajax 获取教师详细信息
def get_teacher_info(request):
    data = {'message': False, 'note': '查询不到该用户！'}
    if request.method == 'POST':
        number = request.POST.get('number') # 工号
        #   查询教师姓名
        sql = "select TeacherName from TMBasicInfo where TeacherNo='%s'"%number
        data_name = execute_sql_11(sql)
        #   如果查询到结果，继续查询所属单位
        if data_name:
            sql = "select InstituteName from BDInstitute where BDInstituteID " \
                "in( select BDInstituteID from BDStaffRoom where BDStaffRoomID " \
                "in( select BDStaffRoomID from TMBasicInfo where TeacherNo='%s'))"%number
            data_institute = execute_sql_11(sql)
            if data_institute:
                data = data_name[0]
                data.update(data_institute[0])
    return JsonResponse(data, safe=False)


# 删除admin用户
def del_admin(request):
    result_data = {}
    if request.method == 'POST':
        delete_array = request.POST.get('delete_array')
        delete_array = list(filter(None, delete_array.split(',')))  # 将字符串分割成数组
        for id in delete_array:
            UserProfile.objects.filter(id=id).delete()
        result_data["message"] = True
        result_data["note"] = '操作成功！删除%s个用户！'%len(delete_array)
    return JsonResponse(data=result_data, safe=False)


# 获取耗材、仪器下级审核人和当前学期（学院领导）
def get_examine(request):
    examine_list = []
    if request.method == "GET":
        examine = UserProfile.objects.filter(admin_rank="学院领导")
        examine = model_to_dic(examine)
        for user in examine:
            examine_list.append({"admin_name": user.get("username"),
                                 "term": get_term().get("now_term")})
    return JsonResponse(examine_list, safe=False)