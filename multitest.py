import multiprocessing
import time
import urllib2
import re
import datetime
import sqlite3
import requests
from bs4 import BeautifulSoup
from get_data_sinastock import *


# FinanceAnalyze web address
# db_name = "FinanceAnalyze"
# fi_url_sina = {}
# fi_url_sina['profit'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml'
# fi_url_sina['operation'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/operation/index.phtml'
# fi_url_sina['grow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/grow/index.phtml'
# fi_url_sina['debtpaying'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/debtpaying/index.phtml'
# fi_url_sina['cashflow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/cashflow/index.phtml'
# fi_url_sina['main'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml'
# fi_url_sina['performance'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml'
# fi_url_sina['news'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/news/index.phtml'
# fi_url_sina['incomedetail'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/incomedetail/index.phtml'
baseurl= "http://www.xicidaili.com/nn/"
# headers = {'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
#                'Accept - Encoding':'gzip, deflate, br',
#                'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
#                'Connection':'Keep-Alive',
#                'Host':'hm.baidu.com',
#                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
# response = requests.get(baseurl, headers=headers)
# response.raise_for_status()
# response.encoding = response.apparent_encoding
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# tr_context = soup.find_all('tr')
# for tr in tr_context:
#     line_tostr = []
#     line = tr.get_text().encode('utf-8').split('\n')
#     print line


def get_data():
    for i in range(1,2):
        url= baseurl+str(i)
        print url
        headers = {'Accept': '*/*',
                   'Accept - Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Connection': 'Keep-Alive',
                   'Cookie':'HMACCOUNT=5FF09B7122E115A4; BIDUPSID=10C09A463C07BBE4E7A26A579D3EF8B5; PSTM=1505741315; MCITY=-315%3A; BDUSS=dmakdiNEtBbmwwTFNXSThCR3ZkOWg5OXZYc2tqUmdmek5iZkU0SWZ4UjB3WVJiQVFBQUFBJCQAAAAAAAAAAAEAAAAONss9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHQ0XVt0NF1beG; BAIDUID=C1828B5B99646A97118F8373C15A5455:FG=1; __guid=259800083.1048035666856329700.1537521324157.1096; BDRCVFR[PaHiFN6tims]=9xWipS8B-FspA7EnHc1QhPEUf; PSINO=1; H_PS_PSSID=; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; monitor_count=5; ZD_ENTRY=baidu; BCLID=8508138960989631378; BDSFRCVID=mv-sJeC627PJVq776BSQheKyp250oYTTH6aokam-eBTb38fAGVJkEG0PDU8g0Kub-jINogKKL2OTHmoP; H_BDCLCKID_SF=tJIfVC-KJD83j-bmKKT0M-FjMfQXKPo0aIKX3buQbpk2qpcNLTDKj6FRy4cXt55Ga2c30lvX-IJKhfjmDpO1j4_eWM7zat6gyeufVluy-fQSbh5jDh38XjksD-Rt5J5UaJby0hvcBIocShnzhp00D63-DH8DqTks56nb3RTs26rjDnCrhJDVKUI8LNDHthOZQjCf_KQPLMjseqvwK5KhD-443bO7ttoy2K6LsR5PQn_5bbQqQpjkMUL1Db3RL6vMtg3t3j6_WlroepvoX55c3MkDhn0E5bj2qRuD_KLK3J; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1537522839|',
                   'Host':'hm.baidu.com',
                   'If-None-Match':'85daf65dfc58b1572717b2fbcb134fd7',
                   'Referer':'http://www.xicidaili.com/nn/1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        html = response.text
        print html
        soup = BeautifulSoup(html, 'html.parser')
        page_data = []
        tr_context = soup.find_all('tr')
        for tr in tr_context:
            line_tostr = []
            line = tr.get_text().encode('utf-8').split('\n')
            print line
            # while '' in line:
            #     line.remove('')
            # line.insert(0, quater)
            # line.insert(0, year)
            # for i in line:
            #     line_tostr.append('"' + i + '"')
            # # print "("+",".join(line_tostr)+")"
            # page_data.append("(" + ",".join(line_tostr) + ")")


def excute_1(table):
    start_year = 2013
    end_year = 2017
    frist_quarter = 1
    end_quarter = 4
    address = fi_url_sina[table]
    table = table
    while start_year <= end_year:
        start_quarter = frist_quarter
        while start_quarter <= end_quarter:
            for page in range(1, 100):
                # print address
                result = get_data(address, str(start_year), str(start_quarter), str(page))
                if result:
                # for i in result:
                #     print i
                    # print address
                    print table, " year:", start_year, "quarter:", start_quarter, "page:", page
                    insert_data(db_name, table, result)
                else:
                    print "no sinadata",table , "   ",start_year,"     ", start_quarter,"     ", page
                    break
            start_quarter = start_quarter + 1
        start_year = start_year + 1


if __name__ == "__main__":
    # create_db(db_name, fi_url_sina)
    p1 = multiprocessing.Process(target = get_data)
    # p2 = multiprocessing.Process(target = excute_1, args = ("operation",))
    # p3 = multiprocessing.Process(target = excute_1, args = ("grow",))
    # p4 = multiprocessing.Process(target = excute_1, args= ("debtpaying",))
    # p5 = multiprocessing.Process(target = excute_1, args= ("cashflow",))
    # p6 = multiprocessing.Process(target = excute_1, args= ("main",))
    # p7 = multiprocessing.Process(target = excute_1, args= ("performance",))

    p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p6.start()
    # p7.start()

    # print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    # for p in multiprocessing.active_children():
    #     print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    # print "END!!!!!!!!!!!!!!!!!"