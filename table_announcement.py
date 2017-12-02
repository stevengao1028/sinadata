# -*- coding: utf-8 -*-
import urllib2
import re
import sqlite3
import requests
import datetime

conn = sqlite3.connect('stock_info.db')
cursor = conn.cursor()
conn.text_factory = str
try:
    cursor.execute(
        'create table IF NOT EXISTS announcement (stock_code varchar(20) , stock_name varchar(20), type varchar(20),'
        ' report_date varchar(20), report_quater varchar(20), report_context varchar(20), quater_last varchar(20),'
        'increase varchar(20),year varchar(20),quarter varchar(20))')
except:
    print "db is exist"
    pass


def announce_data_todb(address,year,quater):
    url = address
    year = year
    quater = quater
    sql = 'INSERT INTO announcement values (?,?,?,?,?,?,?,?,?,?)'
    # try:
    response = requests.get(url)
    response.raise_for_status()
    # except requests.RequestException as e:
    #     return "error_url"+url
    response.encoding = response.apparent_encoding
    html = response.text
    # print html
    lable_pattern = re.compile(r'<td.*</td>')
    lines= re.findall(lable_pattern,html)
    # print lines
    code_pattern = re.compile(r'^\d{6}$')
    tag = 0
    stock_code,stock_name,type,report_date,report_quater,report_context,quater_last,increase = "","","","","","","",""
    for line in lines:
        line_text = re.sub(r'<td style=.*">|<span.*>|<a href=.*">|</a>|</span>|</td>|<td>|<td><a href=.*>', '', line)
        if  re.match(code_pattern, line_text):
            stock_code = line_text
        elif tag == 1:
            stock_name = line_text
        elif tag == 2:
            type = line_text
        elif tag == 3:
            report_date = line_text
        elif tag == 4:
            report_quater = line_text
        elif tag == 5:
            report_context = line_text
        elif tag == 6:
            quater_last = line_text
        elif tag == 7:
            increase = line_text
        else :
            pass
        if tag < 8:
            tag = tag +1
        else:
            tag = 0
            print stock_code,stock_name,type,report_date,report_quater,report_context,quater_last,increase,year,quater
            try:
                report_info = (stock_code,stock_name,type,report_date,report_quater,report_context,quater_last,increase,year,quater)
                cursor.execute(sql, report_info)
                conn.commit()
            except sqlite3.Error, e:
                conn.rollback()
                return "fault"
    return  "sucess"


now_time = datetime.datetime.now()
now_month = now_time.month
now_year = now_time.year
if now_month <=3:
    now_quarter = 1
elif now_month >3 and now_month <=6:
    now_quarter = 2
elif now_month >6 and now_month <=9:
    now_quarter = 3
else:
    now_quarter = 4

for page in range(1, 50):
    address = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?p='+str(page)
    print address
    # print "year:",start_year,"quarter:",start_quarter,"page:",page
    result = announce_data_todb(address,str(now_year),str(now_quarter))
    if result != "sucess":
        print "fault"+address
conn.close()
#
# address='http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?s_i=&s_a=&s_c=&reportdate=2011&quarter=1&p=14'
# print profit_data_todb(address,'2011','1')