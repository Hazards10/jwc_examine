from django.shortcuts import render
from django.forms.models import model_to_dict
from main_app import models
from django.http import HttpResponse
from django.http import JsonResponse
import time
from django.core.cache import cache


def page_login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index_main.html')


def apply_list(request):
    return render(request, 'request_list.html')


def add_hc_view(request):
    return render(request, 'commit/commit_hc.html')


def add_yq_view(request):
    return render(request, 'commit/commit_yq.html')


def examine_hc_1_view(request):
    return render(request, 'check/check_hc_1.html')


def examine_yq_1_view(request):
    return render(request, 'check/check_yq_1.html')


def examine_hc_1_single_view(request):
    return render(request, 'check/check_hc_1_single.html')


def examine_yq_1_single_view(request):
    return render(request, 'check/check_yq_1_single.html')


def examine_hc_2_view(request):
    return render(request, 'check/check_hc_2.html')

def examine_hc2_view_buy(request):
    return render(request, 'check/check_hc_2_buy.html')

def examine_hc2_view_deposit(request):
    return render(request, 'check/check_hc_2_deposit.html')

def examine_yq_2_view(request):
    return render(request, 'check/check_yq_2.html')

def examine_yq2_view_buy(request):
    return render(request, 'check/check_yq_2_buy.html')

def examine_yq2_view_deposit(request):
    return render(request, 'check/check_yq_2_deposit.html')

def examine_hc_2_single_view(request):
    return render(request, 'check/check_hc_2_single.html')


def examine_yq_2_single_view(request):
    return render(request, 'check/check_yq_2_single.html')


def show_hc_creator(request):
    return render(request, 'show/show_hc_creator.html')


def show_yq_creator(request):
    return render(request, 'show/show_yq_creator.html')


def show_hc_examine(request):
    return render(request, 'show/show_hc_examine.html')


def show_yq_examine(request):
    return render(request, 'show/show_yq_examine.html')


def show_hc_admin(request):
    return render(request, 'show/show_hc_all.html')


def show_hc_admin_buy(request):
    return render(request, 'show/show_hc_admin_buy.html')


def show_hc_admin_deposit(request):
    return render(request, 'show/show_hc_admin_deposit.html')


def show_yq_admin(request):
    return render(request, 'show/show_yq_all.html')

def show_yq_admin_buy(request):
    return render(request, 'show/show_yq_admin_buy.html')


def show_yq_admin_deposit(request):
    return render(request, 'show/show_yq_admin_deposit.html')


