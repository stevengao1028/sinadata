# -*- coding: utf-8 -*-
import urllib2
import re
import sqlite3
import requests
import datetime
from bs4 import BeautifulSoup



def get_columes(address):
    url = address
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html = response.text
    # print type(html)
    lable_pattern = re.compile('<tr (.*?)">(.*?)</tr>', re.S)
    lines = re.findall(lable_pattern, html)
    # print lines
    colume_pattern = re.compile(r'<!--(.*?)-->|<td(.*?)>|</td>|</a>|<a(.*?)>|(^\s*)|(\s*$)')
    colume = []
    # print type(lines)
    for line in range(len(lines)):
        if line ==0 :
            for line in lines[line]:
                each_colume = re.sub(colume_pattern, '', line)
                if each_colume:
                    colume.append(each_colume.encode("UTF-8"))
                    print each_colume

    # print lines[0][1]
    # table_title = lines[0][1].split('\n')
    # # print type(table_title)
    # # colume_pattern = re.compile(r'[^\u4e00-\u9fa5]')
    # colume_pattern = re.compile(r'<!--(.*?)-->|<td(.*?)>|</td>|</a>|<a(.*?)>|(^\s*)|(\s*$)')
    # colume =[]
    # for line in table_title:
    #     each_colume = re.sub(colume_pattern,'',line)
    #     if each_colume:
    #         colume.append(each_colume.encode("UTF-8"))
    # return colume


#FinanceAnalyze web address
fi_url_sina = {}
fi_url_sina['profit'] =  'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml'
fi_url_sina['operation'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/operation/index.phtml'
fi_url_sina['grow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/grow/index.phtml'
fi_url_sina['debtpaying'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/debtpaying/index.phtml'
fi_url_sina['cashflow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/cashflow/index.phtml'
fi_url_sina['main'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml'
fi_url_sina['performance'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml'
fi_url_sina['news'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/news/index.phtml'
fi_url_sina['incomedetail'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/incomedetail/index.phtml'

#create table
# db_name = "FinanceAnalyze"
# response = requests.get(fi_url_sina['profit'])
# response.raise_for_status()
# response.encoding = response.apparent_encoding
# html = response.text
# soup = BeautifulSoup(html,'html.parser')
# # print(soup.get_text())
# data = []
# tr_context = soup.find_all('tr')
# for tr in tr_context:
#     # print type(tr.get_text())
#     line = ",".join(tr.get_text().encode('utf-8').split('\n')).lstrip(',').rstrip(',')
#     # sql_value_line = line.lstrip(',').rstrip(',')
#     # print line
#     data.append(line)
#
# response = requests.get(fi_url_sina['news'])
# response.raise_for_status()
# response.encoding = response.apparent_encoding
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
#
# colume = soup.thead.get_text().encode('utf-8').split('\n')
# while '' in colume:
#     colume.remove('')

    # print type(line)
    # if tr.get_text():
    #     print tr.get_text()
        # line.append(tr.get_text())
    # else:
    #     data.append(line)
# print type(line[1])
# print type(line[1].split('\n'))
# # a =0
# while '' in colume:
#     colume.remove('')
# print type(data)
# for i in colume:
#     print i


colume = get_columes(fi_url_sina['news'])
# for i in colume:
#     print i
# for each_address in fi_url_sina:
#     create_table(db_name,each_address)
#     print fi_url_sina[each_address]
# insert_columes = get_columes(fi_url_sina['incomedetail'])
    # add_columes(db_name,each_address,insert_columes)
#get data from sina

