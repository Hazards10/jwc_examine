# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/5/21  20:45'

from datetime import datetime


def get_term():
    """
    通过获取当前时间，返回当前学期和上一个学期
    :return: 包含当前学期和上一个学期的字典
    """
    year = datetime.now().year
    month = datetime.now().month
    term = dict()
    # 在2月份和8月份之间为第二学期，其他月份为第一学期
    if 2 <= month <= 8:
        term["last_term"] = str(year - 1) + '-1'
        term["now_term"] = str(year-1)+'-2'
    else:
        term["last_term"] = str(year - 1) + '-2'
        term["now_term"] = str(year) + '-1'
    return term


if __name__ == "__main__":
    print(get_term().get("now_term"))

