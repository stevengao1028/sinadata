# -*- coding: utf-8 -*-
import urllib2
import re
import datetime
import sqlite3
import requests
from bs4 import BeautifulSoup


def create_db(db,address):
    db_name = db
    url = address
    # print url
    for each_url in url:
        add_table(db_name, each_url)
        insert_columes = get_columes(url[each_url])
        add_columes(db_name, each_url,insert_columes)

def add_table(db,table):
    db_name = db+".db"
    table_name = table
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    conn.text_factory = str
    create_table_sql = 'create table IF NOT EXISTS '+table_name+'  (year varchar(20))'
    try:
        cursor.execute(create_table_sql)
        result = "sucessful"
    except:
        result = table_name+" created fault"
    finally:
        conn.close()
        return result

#columes must be  list
def add_columes(db,table,columes):
    db_name = db + ".db"
    table_name = table
    alert_colume = columes
    print type(alert_colume)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    conn.text_factory = str
    result = ""
    for each_colume in alert_colume:
        print each_colume
        if each_colume =="股票代码" or each_colume == "股票名称":
            add_columes_sql = 'ALTER  TABLE ' + table_name + ' ADD COLUMN  "' + each_colume + '" varchar(20)'
        else:
            add_columes_sql = 'ALTER  TABLE ' + table_name + ' ADD COLUMN  "'+each_colume+'" float(5)'
        print add_columes_sql
        try:
            cursor.execute(add_columes_sql)
            conn.commit()
            result = "sucessful"
        except:
            result = alert_colume[each_colume] + ","
    if result != "sucessful":
        result = result.rstrip(',') + " add fault"
    conn.close()
    return result

#page_data must be a list
def insert_data(db,table,page_data):
    db_name = db + ".db"
    table_name = table
    insert_data = page_data
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    conn.text_factory = str
    insert_data_sql = 'INSERT INTO '+table_name+' VALUES '+ ",".join(insert_data)
    print insert_data_sql
    result = ""
    try:
        cursor.execute(insert_data_sql)
        conn.commit()
        result = "sucessful"
    except:
        db.rollback()
        result = "sinadata insert fault"
    finally:
        conn.close()
        return result


#term must be list
def search_data(db, table, term):
    db_name = db + ".db"
    table_name = table
    search_term = term
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    conn.text_factory = str
    search_data_sql = ' SELECT * FROM ' + table_name + ' where '
    for each_term in search_term:
        search_data_sql = search_data_sql+each_term+search_term[each_term]+" and "
    search_data_sql =search_data_sql[:-4]
    # print search_data_sql
    try:
        cursor.execute(search_data_sql)
        result = cursor.fetchall()
    except :
        result = "no result or condition error"
    finally:
        conn.close()
        return result

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


def get_data(address,year):
    url = address+str(year)
    # try:
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.get_text())
    page_data = []
    tr_context = soup.find_all('tr')
    for tr in tr_context:
        line_tostr = []
        line = tr.get_text().encode('utf-8').split('\n')
        while '' in line:
            line.remove('')
        line.insert(0, year)
        for i in line:
            line_tostr.append('"'+i+'"')
        # print "("+",".join(line_tostr)+")"
        page_data.append("("+",".join(line_tostr)+")")
    # colume = page_data[0].lstrip('(').rstrip(')').split(',')
    # del colume[0]
    # del colume[0]
    del page_data[0]
    return  page_data


# FinanceAnalyze web address
db_name = "Finance"
fi_url_sina = {}
fi_url_sina['profit'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?s_i=&s_a=&s_c=&quarter=4&num=10000&reportdate='
# fi_url_sina['operation'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/operation/index.phtml'
# fi_url_sina['grow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/grow/index.phtml'
# fi_url_sina['debtpaying'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/debtpaying/index.phtml'
# fi_url_sina['cashflow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/cashflow/index.phtml'
# fi_url_sina['main'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml'
# fi_url_sina['performance'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml'
# fi_url_sina['news'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/news/index.phtml'
# fi_url_sina['incomedetail'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/incomedetail/index.phtml'




if __name__ == "__main__":
    create_db(db_name,fi_url_sina)
    years = ['2010','2011','2012','2013','2014','2015','2016','2017']
    # years = ['2016', '2017']
    for year in years:
        print year
        result = get_data(fi_url_sina['profit'],year)
        insert_data(db_name, "profit", result)







