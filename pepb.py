# -*- coding: utf-8 -*-
import urllib2
import re,json
import datetime
import sqlite3
import requests
from bs4 import BeautifulSoup
from get_data_sinastock import *

def get_columes(address):
    url = address
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    colume = soup.thead.get_text().encode('utf-8').split('\n')
    while '' in colume:
        colume.remove('')
    return colume

def get_data_p(address):
    url = address
    page_data = []
    # try:
    response = requests.get(url,)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html = response.text.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # print response.text
    ptn = re.compile('\{.*\}', re.DOTALL)
    rslt = ptn.findall(html)
    # print type(rslt)
    # print(type(rslt[0]))
    return  rslt[0]
def parse_js(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    obj = eval(expr, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
    # c= eval(expr)
    # print obj[0]
    result = json.dumps(obj)
    return result

def json_to_list(expr):
    columes = []
    for x in expr[0]:
        columes.append(x.encode("utf-8"))
    # print columes
    # add_table("FinanceAnalyze", "PE")
    # add_columes("FinanceAnalyze", "PE", columes)
    print type(expr)
    for i in expr:
        row = []
        for key in i:
            row.append(i[key])
        print row

x = get_data_p("http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList['yl3d4qagkRhWInMj']/Market_Center.getHQNodeDataNew?page=1&num=50&sort=per_d&asc=0&node=hs_a")
y = get_data_p("http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList['_y4HiBuMc6BZKJj9']/Market_Center.getHQNodeDataNew?page=1&num=50&sort=pb&asc=0&node=hs_a")

# print (parse_js(x))
print type(parse_js(x))
json_to_list(json.loads(parse_js(x)))
# address = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml'
#
# print get_data(address,"2017","3",1)