from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import time
import json

from main_app import models
from users.models import UserProfile
from utils.date_tool import get_term


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
        creator = json.loads(request.COOKIES.get("user"))
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
            examine = UserProfile.objects.filter(admin_rank="学院领导")
            return render(request, 'commit/commit_hc.html', {'script': "alert", 'wrong': '提交成功', "examines":
                                                             examine, "term": get_term().get("now_term")})


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
        # 将cookies转换为中文
        creator = json.loads(request.COOKIES.get("user"))
        examine = request.POST.get("examine")
        data_type = request.POST.get("data_type")
        course_name = request.POST.get("course_name")
        experiment_name = request.POST.get("experiment_name")
        class_name = request.POST.get("class_name")
        experiment_number = request.POST.get("experiment_number")
        # 日志添加
        add_log_self(creator, examine, data_type)
        models.CheckFormHC.objects.create(date=date, term=term, data_name=data_name, data_parameter=data_parameter,
                                          data_company=data_company, data_count=data_count, data_price=data_price,
                                          data_price2=data_price2, data_usedate=data_usedate, data_person=data_person,
                                          data_remark=data_remark, creator=creator, examine=examine, course_name=
                                          course_name, experiment_name=experiment_name, class_name=class_name,
                                          experiment_number=experiment_number)
        if request.is_ajax():
            return JsonResponse({"message": True}, safe=False)
        else:
            examine = UserProfile.objects.filter(admin_rank="学院领导")
            return render(request, 'commit/commit_hc.html', {'script': "alert", 'wrong': '提交成功', "examines":
                                                             examine, "term": get_term().get("now_term")})


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