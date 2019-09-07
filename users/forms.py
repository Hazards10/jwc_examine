# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/9/4  20:36'

from django import forms


# 登录验证form
class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, required=True)
    password = forms.CharField(min_length=2, required=True)