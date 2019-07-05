# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/5/1  12:40'
import pymssql  #引入mssql库，连接SqlServer数据库


#execute_sql_11方法只做了查询功能，如果有插入数据需求，请参考execute_sql_12方法做修改
def execute_sql_11(sql):
    """
    连接sqlserver，并执行SQL语句（11服务器）
    :param sql: 字符串形式的sql语句
    :return: 返回执行后的结果
    """
    conn = pymssql.connect(host='59.72.194.11', database='TeachBS', user='teachsoap', password='teachsoapjwc2017',
                           as_dict=True,autocommit=True)
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    #print(data)
    conn.close()
    return data

def execute_sql_12(type,sql):
    """
    连接sqlserver，并执行SQL语句(12服务器)
    :param type: 为True返回执行结果，为Flase时不返回执行结果（因为返回执行结果会出错）
    :param sql: 字符串形式的sql语句
    :return: 返回执行后的结果
    """
    conn = pymssql.connect(host='59.72.194.12', database='jwc', user='jwc', password='adsjk3478fhjJ',
                           as_dict=True, autocommit=True)
    cur = conn.cursor()
    cur.execute(sql)
    if type==True:
        data = cur.fetchall()
        print(data)
        return data
    elif type==False:
        row = cur.rowcount
        print(row)
        return row
    conn.close()
