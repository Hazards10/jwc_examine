# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/8/23  16:42'
from django.http import JsonResponse

from main_app import models  # 引入仪器表


def del_hc(request):
    data = {}
    if request.is_ajax()and request.method == "POST":
        del_list = request.POST.get("delStr", None)
        if del_list:
            del_list = list(filter(None, del_list.split(',')))
            del_list_length = len(del_list)
            for id in del_list:
                models.CheckFormHC.objects.filter(data_id=id).delete()
            data["note"] = "删除了%s条数据！" % (str(del_list_length))
            data["message"] = True
    return JsonResponse(data=data, safe=False)


def del_yq(request):
    pass
