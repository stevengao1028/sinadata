# -*- coding: utf-8 -*-
import urllib2
import re
import sqlite3

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




url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?s_i=&s_a=&s_c=&reportdate=2013&quarter=4&p=5'
year = '2015'
quater = '3'
sql = 'INSERT INTO profit values (?,?,?,?,?,?,?,?,?,?,?)'
response = urllib2.urlopen(url)
html = response.read()
html = unicode(html, "gb2312").encode("utf8")  #gb2312--->utf-8
lable_pattern = re.compile('<td.*</td>')
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
