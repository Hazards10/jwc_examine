# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/8/23  16:55'
from django.forms.models import model_to_dict


def model_to_dic(data_info):
    data_list = []
    for i in range(0, len(data_info)):
        temp_data = model_to_dict(data_info[i])
        data_list.append(temp_data)

    return data_list