# -*- coding: utf-8 -*-
import urllib2
import re
import sqlite3
import requests

conn = sqlite3.connect('stock_info.db')
cursor = conn.cursor()
conn.text_factory = str
try:
    cursor.execute(
        'create table profit (stock_code varchar(20) , stock_name varchar(20), roe varchar(20),'
        ' netprofitmargin varchar(20), profitmargin varchar(20), netprofit varchar(20), eps varchar(20),'
        'income varchar(20),mips varchar(20),year varchar(20),quarter varchar(20))')
except:
    # print "db is exist"
    pass


def profit_data_todb(address,year,quater):
    url = address
    year = year
    quater = quater
    sql = 'INSERT INTO profit values (?,?,?,?,?,?,?,?,?,?,?)'
    # try:
    response = requests.get(url)
    # response.raise_for_status()
    # except requests.RequestException as e:
    #     return "error_url"+url
    response.encoding = response.apparent_encoding
    html = response.text
    lable_pattern = re.compile(r'<td.*</td>')
    lines= re.findall(lable_pattern,html)
    code_pattern = re.compile(r'^\d{6}$')
    tag = 0
    stock_code,stock_name,roe,netprofitmargin,profitmargin,netprofit,eps,income,mips = "","","","","","","","",""
    for line in lines:
        line_text = re.sub(r'<td>|</td>|<td.*_blank">|</a>|<td style=.*$|<a href=.*', '', line)
        # print line_text
        if  re.match(code_pattern, line_text):
            stock_code = line_text
        elif tag == 1:
            stock_name = line_text
        elif tag == 2:
            roe = line_text
        elif tag == 3:
            netprofitmargin = line_text
        elif tag == 4:
            profitmargin = line_text
        elif tag == 5:
            netprofit = line_text
        elif tag == 6:
            eps = line_text
        elif tag == 7:
            income = line_text
        elif tag == 8:
            mips = line_text
        else :
            pass
        if tag < 8:
            tag = tag +1
        else:
            tag = 0
            print stock_code,stock_name, roe,netprofitmargin,profitmargin,netprofit,eps,income,mips,year,quater
            try:
                profit_info = (stock_code,stock_name,roe,netprofitmargin,profitmargin,netprofit,eps,income,mips,year,quater)
                cursor.execute(sql, profit_info)
                conn.commit()
            except sqlite3.Error, e:
                conn.rollback()
                return "fault"
    return  "sucess"



start_year = 2016
end_year = 2017
start_quarter = 1
end_quarter = 4
while start_year <= end_year:
    start_quarter = 1
    while start_quarter <= end_quarter:
        for page in range(1, 100):
            address = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?s_i=&s_a=&s_c=&reportdate='+str(start_year)+'&quarter='+str(start_quarter)+'&p='+str(page)
            print address
            # print "year:",start_year,"quarter:",start_quarter,"page:",page
            result = profit_data_todb(address,str(start_year),str(start_quarter))
            if result != "sucess":
                print "fault"+address
        start_quarter = start_quarter + 1
    start_year = start_year + 1
conn.close()
#
# address='http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?s_i=&s_a=&s_c=&reportdate=2011&quarter=1&p=14'
# print profit_data_todb(address,'2011','1')