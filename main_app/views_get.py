# -*- coding: utf-8 -*-
from django.forms.models import model_to_dict
from django.http import JsonResponse

from main_app import models     # 引入项目中的模型表
from utils.execute_sql import  execute_sql_11   # 引入连接11数据库的方法


def model_to_dic(data_info):
    data_list = []
    for i in range(0, len(data_info)):
        temp_data = model_to_dict(data_info[i])
        data_list.append(temp_data)

    return data_list


# 得到通用申请列表
def get_sender(request):
    if request.is_ajax():
        user_b = request.POST.get('user_b')
        data_info = models.Log.objects.filter(B=user_b)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 得到第一级通过审核表(HC) for creator
def get_pass1_list_hc(request):
    if request.is_ajax():
        creator_name = request.POST.get('creator')
        filter_dic = dict()
        filter_dic['creator'] = creator_name
        filter_dic['check_1'] = True
        check_data = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第一级通过审核表(YQ) for creator
def get_pass1_list_yq(request):
    if request.is_ajax():
        creator_name = request.POST.get('creator')
        filter_dic = dict()
        filter_dic['creator'] = creator_name
        filter_dic['check_1'] = True
        check_data = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第二级通过审核表(HC) for examine
def get_pass2_list_hc(request):
    if request.is_ajax():
        examine = request.POST.get('examine')
        filter_dic = dict()
        filter_dic['examine'] = examine
        filter_dic['check_2'] = True
        check_data = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第二级通过审核表(YQ) for examine
def get_pass2_list_yq(request):
    if request.is_ajax():
        examine = request.POST.get('examine')
        filter_dic = dict()
        filter_dic['examine'] = examine
        filter_dic['check_2'] = True
        check_data = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第一级待审核表(HC) for examine
def get_examine_list_hc(request):
    if request.is_ajax():
        examine_name = request.POST.get('examine_name')
        check_data = models.CheckFormHC.objects.filter(examine=examine_name)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第一级待审核表(YQ) for examine
def get_examine_list_yq(request):
    if request.is_ajax():
        examine_name = request.POST.get('examine_name')
        check_data = models.CheckFormYQ.objects.filter(examine=examine_name)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第一级待审核表(HC)single
def get_examine_single_list_hc(request):
    if request.is_ajax():
        creator_name = request.POST.get('creator_name')
        examine_name = request.POST.get('examine_name')
        filter_dic = dict()
        filter_dic['creator'] = creator_name
        filter_dic['examine'] = examine_name
        check_data = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第一级待审核表(YQ)single
def get_examine_single_list_yq(request):
    if request.is_ajax():
        creator_name = request.POST.get('creator_name')
        examine_name = request.POST.get('examine_name')
        filter_dic = dict()
        filter_dic['creator'] = creator_name
        filter_dic['examine'] = examine_name
        check_data = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第二级待审核表(HC)
def get_second_examine_list_hc(request):
    if request.is_ajax():
        check_data = models.CheckFormHC.objects.filter(check_1=True)
        return JsonResponse(model_to_dic(check_data), safe=False)

# 得到第二级购买待审核（HC）
def get_second_examine_buy_list_hc(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        check_data = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)

# 得到第二级入库待审核（HC）
def get_second_examine_deposit_list_hc(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_buy'] = True
        check_data = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)

# 得到第二级待审核表(YQ)
def get_final_list_yq(request):
    if request.is_ajax():
        check_data = models.CheckFormYQ.objects.filter(check_1=True)
        return JsonResponse(model_to_dic(check_data), safe=False)

# 得到第二级购买待审核（YQ）
def get_second_examine_buy_list_yq(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        check_data = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)

# 得到第二级入库待审核（YQ）
def get_second_examine_deposit_list_yq(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_buy'] = True
        check_data = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)

# 得到第二级待审核表(HC)single
def get_final_single_list_hc(request):
    if request.is_ajax():
        examine_name = request.POST.get('examine_name')
        admin_name = request.POST.get('admin_name')
        filter_dic = dict()
        filter_dic['examine'] = examine_name
        filter_dic['admin'] = admin_name
        check_data = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 得到第二级待审核表(YQ)single
def get_final_single_list_yq(request):
    if request.is_ajax():
        examine_name = request.POST.get('examine_name')
        admin_name = request.POST.get('admin_name')
        filter_dic = dict()
        filter_dic['examine'] = examine_name
        filter_dic['admin'] = admin_name
        check_data = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)


# 显示当前用户提交过的审核表(HC) for creator
def show_check_hc_creator(request):
    if request.is_ajax():
        creator_name = request.POST.get("creator")
        filter_dic = dict()
        filter_dic['creator'] = creator_name
        data_info = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示学院审核过的审核表(HC) for examine
def show_check_hc_examine(request):
    if request.is_ajax():
        examine_name = request.POST.get("examine_name")
        filter_dic = dict()
        filter_dic['examine'] = examine_name
        filter_dic['check_1'] = True
        data_info = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示当前用户创建的审核表(YQ) for creator
def show_check_yq_creator(request):
    if request.is_ajax():
        creator_name = request.POST.get("creator")
        filter_dic = dict()
        filter_dic['creator'] = creator_name
        data_info = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示学院审核过的审核表(YQ) for examine
def show_check_yq_examine(request):
    if request.is_ajax():
        examine_name = request.POST.get("examine_name")
        filter_dic = dict()
        filter_dic['examine'] = examine_name
        filter_dic['check_1'] = True
        data_info = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示所有通过的审核表(HC)
def show_check_all_hc(request):
    if request.method == 'POST':
        data_info = models.CheckFormHC.objects.filter(check_2=True)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示教务处审核过的购买审核表(HC) for admin
def show_check_all_hc_buy(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_buy'] = True
        data_info = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示教务处审核过的购买审核表(YQ) for admin
def show_check_all_hc_deposit(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_buy'] = True
        filter_dic['is_deposit'] = True
        data_info = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示所有通过的审核表(YQ)
def show_check_all_yq(request):
    if request.method == 'POST':
        data_info = models.CheckFormYQ.objects.filter(check_2=True)
        return JsonResponse(model_to_dic(data_info), safe=False)

# 显示教务处审核过的购买审核表(YQ) for admin
def show_check_all_yq_buy(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_buy'] = True
        data_info = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示教务处审核过的购买审核表(YQ) for admin
def show_check_all_yq_deposit(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_buy'] = True
        filter_dic['is_deposit'] = True
        data_info = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示所有用户信息
def show_all_admin(request):
    if request.method == 'POST':
        data_info = models.AdminForm.objects.all()
        return JsonResponse(model_to_dic(data_info), safe=False)

#################
### AJAX 接口
#################


# ajax 获取教师详细信息
def get_teacher_info(request):
    if request.method == 'POST':
        number = request.POST.get('number') # 工号
        #   查询教师姓名
        sql = "select TeacherName from TMBasicInfo where TeacherNo='%s'"%number
        data_name = execute_sql_11(sql)
        print('教师姓名',data_name,type(data_name))
        #   如果查询到结果，继续查询所属单位
        data = {}
        if data_name:
            sql = "select InstituteName from BDInstitute where BDInstituteID " \
                "in( select BDInstituteID from BDStaffRoom where BDStaffRoomID " \
                "in( select BDStaffRoomID from TMBasicInfo where TeacherNo='%s'))"%number
            data_institute = execute_sql_11(sql)
            if data_institute:
                data = data_name[0]
                data.update(data_institute[0])
                return JsonResponse(data, safe=False)
            else:
                data = {'message': False, 'note': '查询不到该用户！'}
                return JsonResponse(data, safe=False)
        else:
            data = {'message': False, 'note': '查询不到该用户！'}
            return JsonResponse(data, safe=False)
    else:
        data = {'message':False, 'note':'查询不到该用户！'}
        return JsonResponse(data, safe=False)


# 获取耗材、仪器下级审核人（学院领导）
def get_examine(request):
    if request.method == "GET":
        examine = models.AdminForm.objects.filter(admin_rank="学院领导")
        examine = model_to_dic(examine)
        examine_list = []
        for name in examine:
            examine_list.append(name.get("admin_name"))
        return JsonResponse(examine_list, safe=False)




