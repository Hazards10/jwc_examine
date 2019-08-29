# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.db.models import Q # 用于model复杂条件查询
from django.views.generic.base import View # django视图view，继承他可以重构get、post方法

import time

from main_app import models     # 引入项目中的模型表
from utils.execute_sql import  execute_sql_11   # 引入连接11数据库的方法
from utils.date_tool import get_term
from utils.model_to_dic import model_to_dic


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
        filter_dic['is_deposit'] = True
        filter_dic['is_buy'] = False
        check_data = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)

# 得到第二级入库待审核（HC）
def get_second_examine_deposit_list_hc(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_deposit'] = False
        filter_dic['is_buy'] = False
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
        filter_dic['is_buy'] = False
        filter_dic['is_deposit'] = True
        check_data = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(check_data), safe=False)

# 得到第二级入库待审核（YQ）
def get_second_examine_deposit_list_yq(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_deposit'] = False
        filter_dic['is_buy'] = False
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


# 显示当前用户提交过的审核表(HC) for creator  ajax
def show_check_hc_creator(request):
    result = {}
    if request.is_ajax():
        creator_name = request.POST.get("creator")
        # 过滤数据
        all_result = models.CheckFormHC.objects.filter(creator = creator_name)
        # 数据条数
        recordsTotal = all_result.count()
        recordsFiltered = recordsTotal
        # 第一条数据的起始位置
        start = int(request.POST['start'])
        # 每页显示的长度，默认为10
        length = int(request.POST['length'])
        # 计数器，确保ajax从服务器返回是对应的
        draw = int(request.POST['draw'])
        # 全局收索条件
        new_search = request.POST['search[value]']
        # 排序列的序号
        new_order = request.POST['order[0][column]']
        # 排序列名
        by_name = request.POST['columns[{0}][data]'.format(new_order)]
        # 排序类型，升序降序
        fun_order = request.POST['order[0][dir]']
        # 排序开启，匹配表格列
        if by_name:
            if fun_order == "asc":
                all_result = all_result.order_by(by_name)
            else:
                all_result = all_result.order_by("-{0}".format(by_name))
        # 模糊查询，包含内容就查询
        if new_search:
            all_result = all_result.filter(Q(data_id__contains=new_search) | Q(term__contains=new_search) |
                                           Q(data_name__contains=new_search) | Q(data_parameter__contains=new_search) |
                                           Q(data_company__contains=new_search) | Q(data_count__contains=new_search) |
                                           Q(data_price__contains=new_search)| Q(data_price2__contains=new_search)|
                                           Q(data_usedate__contains=new_search) |
                                           Q(examine__contains=new_search) | Q(check_1__contains=new_search))
        # 获取全部数据
        if length == -1:
            datas = models.CheckFormHC.objects.filter(creator=creator_name)
            recordsTotal = recordsFiltered = 1
        # 切片获取部分数据
        else:
            # 获取首页的数据
            datas = all_result[start:(start + length)]
        # 转为字典
        resp = model_to_dic(datas)
        # 返回计数，总条数，返回数据
        result = {
            'draw': draw,
            'recordsTotal': recordsTotal,
            'recordsFiltered': recordsFiltered,
            'data': resp,
        }
    return JsonResponse(result, safe=False)


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
    result = {}
    if request.is_ajax():
        creator_name = request.POST.get("creator")
        # 过滤数据
        all_result = models.CheckFormYQ.objects.filter(creator=creator_name)
        # 数据条数
        recordsTotal = all_result.count()
        recordsFiltered = recordsTotal
        # 第一条数据的起始位置
        start = int(request.POST['start'])
        # 每页显示的长度，默认为10
        length = int(request.POST['length'])
        # 计数器，确保ajax从服务器返回是对应的
        draw = int(request.POST['draw'])
        # 全局收索条件
        new_search = request.POST['search[value]']
        # 排序列的序号
        new_order = request.POST['order[0][column]']
        # 排序列名
        by_name = request.POST['columns[{0}][data]'.format(new_order)]
        # 排序类型，升序降序
        fun_order = request.POST['order[0][dir]']
        # 排序开启，匹配表格列
        if by_name:
            if fun_order == "asc":
                all_result = all_result.order_by(by_name)
            else:
                all_result = all_result.order_by("-{0}".format(by_name))
        # 模糊查询，包含内容就查询
        if new_search:
            all_result = all_result.filter(Q(data_id__contains=new_search) | Q(term__contains=new_search) |
                                           Q(data_name__contains=new_search) | Q(data_parameter__contains=new_search) |
                                           Q(data_company__contains=new_search) | Q(data_count__contains=new_search) |
                                           Q(data_price__contains=new_search) | Q(data_price2__contains=new_search) |
                                           Q(data_company2__contains=new_search) |
                                           Q(examine__contains=new_search) | Q(check_1__contains=new_search))
        # 获取全部数据
        if length == -1:
            datas = models.CheckFormHC.objects.filter(creator=creator_name)
            recordsTotal = recordsFiltered = 1
        # 切片获取部分数据
        else:
            # 获取首页的数据
            datas = all_result[start:(start + length)]
        # 转为字典
        resp = model_to_dic(datas)
        # 返回计数，总条数，返回数据
        result = {
            'draw': draw,
            'recordsTotal': recordsTotal,
            'recordsFiltered': recordsFiltered,
            'data': resp,
        }
    return JsonResponse(result, safe=False)


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
        filter_dic['is_deposit'] = True
        filter_dic['is_buy'] = True
        data_info = models.CheckFormHC.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示教务处审核过的购买审核表(YQ) for admin
def show_check_all_hc_deposit(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_deposit'] = True
        filter_dic['is_buy'] = False
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
        filter_dic['is_deposit'] = True
        filter_dic['is_buy'] = True
        data_info = models.CheckFormYQ.objects.filter(**filter_dic)
        return JsonResponse(model_to_dic(data_info), safe=False)


# 显示教务处审核过的购买审核表(YQ) for admin
def show_check_all_yq_deposit(request):
    if request.is_ajax():
        filter_dic = dict()
        filter_dic['check_1'] = True
        filter_dic['check_2'] = True
        filter_dic['is_deposit'] = True
        filter_dic['is_buy'] = False
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


# 获取耗材、仪器下级审核人和当前学期（学院领导）
def get_examine(request):
    if request.method == "GET":
        examine = models.AdminForm.objects.filter(admin_rank="学院领导")
        examine = model_to_dic(examine)
        examine_list = []
        for name in examine:
            examine_list.append({"admin_name": name.get("admin_name"),
                                 "term": get_term().get("now_term")})
        return JsonResponse(examine_list, safe=False)


# 普通老师 获取提交的一条数据，或编辑这条数据（耗材）
class GetEditHcCreator(View):
    def get(self, request, *args, **kwargs):
        data = {}
        if request.is_ajax():
            id = request.GET.get("id", None)
            if id:
               data=models.CheckFormHC.objects.filter(data_id=id)
        return JsonResponse(data=model_to_dic(data), safe=False)

    def post(self, request, *args, **kwargs):
        data = {}
        if request.is_ajax():
            term = request.POST.get("term")
            data_name = request.POST.get("data_name")
            data_parameter = request.POST.get("data_parameter")
            data_company = request.POST.get("data_company")
            data_count = request.POST.get("data_count")
            data_price = request.POST.get("data_price")
            data_price2 = request.POST.get("data_price2")
            data_usedate = request.POST.get("data_usedate")
            data_person = request.POST.get("data_person")
            data_remark = request.POST.get("data_remark")
            creator = request.POST.get("creator")
            examine = request.POST.get("examine")
            data_id = request.POST.get("data_id")
            models.CheckFormHC.objects.filter(data_id=data_id).update(term=term, data_name=data_name,
                    data_parameter=data_parameter, data_company=data_company, data_count=data_count,
                    data_person=data_person, data_price=data_price, data_price2=data_price2, data_usedate=data_usedate,
                    data_remark=data_remark,creator=creator,examine=examine,
                    date=time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
                    )
            data["message"] = True
        return JsonResponse(data=data, safe=False)


# 普通老师 获取提交的一条数据，或编辑这条数据（仪器）
class GetEditYqCreator(View):
    def get(self, request, *args, **kwargs):
        data = {}
        if request.is_ajax():
            id = request.GET.get("id", None)
            if id:
               data=models.CheckFormYQ.objects.filter(data_id=id)
        return JsonResponse(data=model_to_dic(data), safe=False)

    def post(self, request, *args, **kwargs):
        data = {}
        if request.is_ajax():
            data_id = request.POST.get("data_id")
            term = request.POST.get("term")
            data_name = request.POST.get("data_name")
            data_parameter = request.POST.get("data_parameter")
            data_company = request.POST.get("data_company")
            data_count = request.POST.get("data_count")
            data_price = request.POST.get("data_price")
            data_price2 = request.POST.get("data_price2")
            creator = request.POST.get("creator")
            examine = request.POST.get("examine")
            models.CheckFormYQ.objects.filter(data_id=data_id).update(term=term, data_name=data_name,
                    data_parameter=data_parameter, data_company=data_company, data_count=data_count,
                    data_price=data_price, data_price2=data_price2, creator=creator,examine=examine,
                    date=time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
                     )
            data["message"] = True
        return JsonResponse(data=data, safe=False)


