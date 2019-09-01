from django.shortcuts import render
from django.http import JsonResponse

import time
import json

from main_app import models


# 创建admin用户
def add_admin(request):
    result_data = {}
    if request.method == 'POST':
        number = request.POST.get('number')  # 工号
        name = request.POST.get('name')     # 姓名
        unit = request.POST.get('unit')     # 单位
        rank = request.POST.get('rank')     # 用户等级
        data = models.AdminForm.objects.filter(admin_teacherNo=number)
        # 判断用户是否已经添加过
        if data:
            result_data["message"] = False
            result_data["note"] = "用户已经存在！"
        # 没有添加过，创建用户
        else:
            models.AdminForm.objects.create(admin_name=name, admin_teacherNo=number, admin_rank =rank, admin_unit=unit)
            result_data["message"] = True
            result_data["note"] = "添加用户成功！"
    return JsonResponse(data=result_data, safe=False)


def edit_admin(request):
    data = {}
    if request.is_ajax():
        admin_id = request.POST.get('edit_adminId')  # 工号
        rank = request.POST.get('rank')     # 用户等级
        if models.AdminForm.objects.filter(admin_id=admin_id).update(admin_rank = rank):
            data["message"] = True
    return JsonResponse(data=data, safe=False)


# 删除admin用户
def del_admin(request):
    result_data = {}
    if request.method == 'POST':
        delete_array = request.POST.get('delete_array')
        delete_array = list(filter(None, delete_array.split(',')))  # 将字符串分割成数组
        for id in delete_array:
            models.AdminForm.objects.filter(admin_id=id).delete()
        result_data["message"] = True
        result_data["note"] = '操作成功！删除%s个用户！'%len(delete_array)
    return JsonResponse(data=result_data, safe=False)


# 添加申请列表(内部函数)
def add_log_self(user_a, user_b, data_type):
    now_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    filter_dic = dict()
    filter_dic['A'] = user_a
    filter_dic['B'] = user_b
    filter_dic['type'] = data_type
    result = models.Log.objects.filter(**filter_dic)
    # 查询到日志更新数据
    if result.count() != 0:
        result.update(date=now_time)
    # 否者创建日志
    else:
        models.Log.objects.create(A=user_a, B=user_b, date=now_time, type=data_type)


# 添加数据(仪器数据)
def add_yq(request):
    if request.method == 'POST':
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        term = request.POST.get("term")
        data_name = request.POST.get("data_name")
        data_company = request.POST.get("data_company")
        data_count = request.POST.get("data_count")
        data_price = request.POST.get("data_price")
        data_price2 = request.POST.get("data_price2")
        data_company2 = request.POST.get("data_company2")
        data_parameter = request.POST.get("data_parameter")
        creator = request.POST.get("creator")
        examine = request.POST.get("examine")
        data_type = request.POST.get("data_type")
        # log添加
        add_log_self(creator, examine, data_type)
        models.CheckFormYQ.objects.create(date=date, term=term, data_name=data_name, data_company=data_company,
                                          data_count=data_count, data_price=data_price, data_price2=data_price2,
                                          data_company2=data_company2, data_parameter=data_parameter,
                                          creator=creator, examine=examine)
        if request.is_ajax():
            return JsonResponse({"message": True}, safe=False)
        else:
            return render(request, 'commit/commit_hc.html', {'script': "alert", 'wrong': '提交成功'})


# 添加数据(耗材数据)
def add_hc(request):
    if request.method == 'POST':
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
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
        data_type = request.POST.get("data_type")
        # 日志添加
        add_log_self(creator, examine, data_type)
        models.CheckFormHC.objects.create(date=date, term=term, data_name=data_name, data_parameter=data_parameter,
                                          data_company=data_company, data_count=data_count, data_price=data_price,
                                          data_price2=data_price2, data_usedate=data_usedate, data_person=data_person,
                                          data_remark=data_remark, creator=creator, examine=examine)
        if request.is_ajax():
            return JsonResponse({"message": True}, safe=False)
        else:
            return render(request, 'commit/commit_hc.html', {'script': "alert", 'wrong': '提交成功'})


# excel导入hc
def excel_commit_hc(request):
    if request.is_ajax():
        data_json = request.POST.get('data_json')
        creator = request.POST.get('creator')
        data = json.loads(data_json)
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        data_type = 0
        # test_data = data[0]
        # standard_list = ["计划编号","材料名称", "规格型号", "单位", "数量", "单价(元)", "金额(元)", "使用日期", "验收领用负责人", "使用学期", "备注", "下级审核人"]
        # test = test_data.keys()
        # print(test, type(test), standard_list, type(standard_list))
        # if operator.eq(test, standard_list):
        for i in range(0, len(data)):
            data_name = data[i].get('材料名称')
            data_parameter = data[i].get('规格型号')
            data_company = data[i].get('单位')
            data_count = data[i].get('数量')
            data_price = data[i].get('单价(元)')
            data_price2 = data[i].get('金额(元)')
            data_usedate = data[i].get('使用日期')
            data_person = data[i].get('验收领用负责人')
            term = data[i].get('使用学期')
            data_remark = data[i].get('备注')
            examine = data[i].get('下级审核人')
            add_log_self(creator, examine, data_type)
            models.CheckFormHC.objects.create(date=date, term=term,
                                data_name=data_name, data_parameter=data_parameter, data_company=data_company,
                                data_count=data_count, data_price=data_price, data_price2=data_price2,
                                data_usedate=data_usedate, data_person=data_person,
                                data_remark=data_remark, creator=creator, examine=examine)
        return JsonResponse("true", safe=False)


# excel导入yq
def excel_commit_yq(request):
    if request.is_ajax():
        data_json = request.POST.get('data_json')
        creator = request.POST.get('creator')
        data = json.loads(data_json)
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        data_type = 1
        # list = ["序号", "设备名称", "规格及技术参数", "单位", "数量", "预算单价(万元)", "预算金额(万元)", "使用单位", "使用学期", "下级审核人"];
        for i in range(0,len(data)):
            data_name = data[i].get('设备名称')
            data_company = data[i].get('单位')
            data_count = data[i].get('数量')
            data_price = data[i].get('预算单价(万元)')
            data_price2 = data[i].get('预算金额(万元)')
            data_company2 = data[i].get('使用单位')
            data_parameter = data[i].get('规格及技术参数')
            term = data[i].get('使用学期')
            examine = data[i].get('下级审核人')
            add_log_self(creator, examine, data_type)
            models.CheckFormYQ.objects.create(date=date, term=term, data_name=data_name, data_company=data_company,
                                              data_count=data_count, data_price=data_price, data_price2=data_price2,
                                              data_company2=data_company2, data_parameter=data_parameter,
                                              creator=creator, examine=examine)
        return JsonResponse("true", safe=False)