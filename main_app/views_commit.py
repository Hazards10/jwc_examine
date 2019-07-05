from main_app import models
from django.http import JsonResponse
from main_app import views_add


# 第一级审核提交(HC)
def commit_check1_hc(request):
    if request.is_ajax():
        index = request.POST.get('data_id')
        user_a = request.POST.get('user_a')
        user_b = request.POST.get('user_b')
        check_1 = request.POST.get('check_1')
        if check_1 == "true":
            models.CheckFormHC.objects.filter(data_id=index).update(check_1=True)
        else:
            models.CheckFormHC.objects.filter(data_id=index).update(check_1=False)
        views_add.add_log_self(user_a, user_b, 0)
        return JsonResponse("true", safe=False)


# 第一级审核提交(YQ)
def commit_check1_yq(request):
    if request.is_ajax():
        index = request.POST.get('data_id')
        user_b = request.POST.get('user_b')
        user_a = request.POST.get('user_a')
        check_1 = request.POST.get('check_1')
        if check_1 == "true":
            models.CheckFormYQ.objects.filter(data_id=index).update(check_1=True)
        else:
            models.CheckFormYQ.objects.filter(data_id=index).update(check_1=False)
        views_add.add_log_self(user_a, user_b, 0)
        return JsonResponse("true", safe=False)


# 第二级审核提交(HC)
def commit_check2_hc(request):
    if request.is_ajax():
        index = request.POST.get('data_id')
        check_2 = request.POST.get('flag')
        admin_name = request.POST.get('admin_name')
        if check_2 == "true":
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['check_2'] = True
            models.CheckFormHC.objects.filter(data_id=index).update(**filter_dic)
        else:
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['check_2'] = False
            models.CheckFormHC.objects.filter(data_id=index).update(**filter_dic)
        return JsonResponse("true", safe=False)

# 第二级审核购买标记提交(HC)
def commit_check2_hc_buy(request):
    if request.is_ajax():
        index = request.POST.get('data_id')
        is_buy = request.POST.get('flag')
        admin_name = request.POST.get('admin_name')
        if is_buy == "true":
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['is_buy'] = True
            models.CheckFormHC.objects.filter(data_id=index).update(**filter_dic)
        else:
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['is_buy'] = False
            models.CheckFormHC.objects.filter(data_id=index).update(**filter_dic)
        return JsonResponse("true", safe=False)

# 第二级审核入库标记提交(HC)
def commit_check2_hc_deposit(request):
    if request.is_ajax():
        index = request.POST.get('data_id')
        is_deposit = request.POST.get('flag')
        admin_name = request.POST.get('admin_name')
        if is_deposit == "true":
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['is_deposit'] = True
            models.CheckFormHC.objects.filter(data_id=index).update(**filter_dic)
        else:
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['is_deposit'] = False
            models.CheckFormHC.objects.filter(data_id=index).update(**filter_dic)
        return JsonResponse("true", safe=False)

# 第二级审核提交(YQ)
def commit_check2_yq(request):
    if request.is_ajax():
        index = request.POST.get('data_id')
        check_2 = request.POST.get('flag')
        admin_name = request.POST.get('admin_name')
        if check_2 == "true":
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['check_2'] = True
            models.CheckFormYQ.objects.filter(data_id=index).update(**filter_dic)
        else:
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['check_2'] = False
            models.CheckFormYQ.objects.filter(data_id=index).update(**filter_dic)
        return JsonResponse("true", safe=False)

# 第二级审核购买标记提交(HC)
def commit_check2_yq_buy(request):
    if request.is_ajax():
        index = request.POST.get('data_id')
        is_buy = request.POST.get('flag')
        admin_name = request.POST.get('admin_name')
        if is_buy == "true":
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['is_buy'] = True
            models.CheckFormYQ.objects.filter(data_id=index).update(**filter_dic)
        else:
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['is_buy'] = False
            models.CheckFormYQ.objects.filter(data_id=index).update(**filter_dic)
        return JsonResponse("true", safe=False)

# 第二级审核入库标记提交(HC)
def commit_check2_yq_deposit(request):
    if request.is_ajax():
        index = request.POST.get('data_id')
        is_deposit = request.POST.get('flag')
        admin_name = request.POST.get('admin_name')
        if is_deposit == "true":
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['is_deposit'] = True
            models.CheckFormYQ.objects.filter(data_id=index).update(**filter_dic)
        else:
            filter_dic = dict()
            filter_dic['admin'] = admin_name
            filter_dic['is_deposit'] = False
            models.CheckFormYQ.objects.filter(data_id=index).update(**filter_dic)
        return JsonResponse("true", safe=False)
