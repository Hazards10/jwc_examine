from django.shortcuts import render
from users.models import UserProfile
from utils.date_tool import get_term


def apply_list(request):
    return render(request, 'request_list.html')


def add_hc_view(request):
    """
    创建新耗材表页视图
    :param request:
    :return:
    """
    examine = UserProfile.objects.filter(admin_rank="学院领导")
    return render(request, 'commit/commit_hc.html', {"examines": examine, "term": get_term().get("now_term") })


def add_yq_view(request):
    """
    创建新仪器表页视图
    :param request:
    :return:
    """
    examine = UserProfile.objects.filter(admin_rank="学院领导")
    return render(request, 'commit/commit_yq.html', { "examines": examine, "term": get_term().get("now_term")})


def examine_hc_1_view(request):
    examine = UserProfile.objects.filter(admin_rank="学院领导")
    return render(request, 'check/check_hc_1.html', { "examines": examine, "term": get_term().get("now_term")})


def examine_yq_1_view(request):
    examine = UserProfile.objects.filter(admin_rank="学院领导")
    return render(request, 'check/check_yq_1.html', { "examines": examine, "term": get_term().get("now_term")})


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


