import multiprocessing
import time
from get_data_sinastock import *


# FinanceAnalyze web address
db_name = "FinanceAnalyze"
fi_url_sina = {}
fi_url_sina['profit'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml'
fi_url_sina['operation'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/operation/index.phtml'
fi_url_sina['grow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/grow/index.phtml'
fi_url_sina['debtpaying'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/debtpaying/index.phtml'
fi_url_sina['cashflow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/cashflow/index.phtml'
fi_url_sina['main'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml'
fi_url_sina['performance'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml'
# fi_url_sina['news'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/news/index.phtml'
# fi_url_sina['incomedetail'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/incomedetail/index.phtml'

def excute_1(table):
    start_year = 2005
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
    p1 = multiprocessing.Process(target = excute_1, args = ("profit",))
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