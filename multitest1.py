import urllib2
import urllib
import random
import math
import urlparse
import time
import cookielib


########################################################################
class Baidu:
    """"""
    Referer = 'http://www.xicidaili.com/nn/3447'
    TargetPage = 'http://www.xicidaili.com'
    BaiduID = ''
    Hjs = "http://hm.baidu.com/hm.js?"
    Hgif = "http://hm.baidu.com/hm.gif?"
    UserAgent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'  # IE9
    MyData = {'cc': '1', 'ck': '1', 'cl': '32-bit', 'ds': '1024x768', 'et': '0', 'ep': '0', 'fl': '11.0', 'ja': '1',
              'ln': 'zh-cn', 'lo': '0', 'nv': '1', 'st': '3', 'v': '1.0.17'}

    # ----------------------------------------------------------------------
    def __init__(self, baiduID, targetPage=None, refererPage=None):
        """Constructor"""
        self.TargetPage = targetPage or self.TargetPage
        self.Referer = refererPage or self.Referer
        self.BaiduID = baiduID
        self.MyData['si'] = self.BaiduID
        self.MyData['su'] = urllib.quote(self.Referer)
        pass

    def run(self, timeout=5):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [("Referer", self.TargetPage), ("User-Agent", self.UserAgent)]
        try:
            response = opener.open(self.Hjs + self.BaiduID).info()
            self.MyData['rnd'] = int(random.random() * 2147483647)
            self.MyData['lt'] = int(time.time())
            fullurl = self.Hgif + urllib.urlencode(self.MyData)
            response2 = opener.open(fullurl, timeout=timeout).info()
            self.MyData['rnd'] = int(random.random() * 2147483647)
            self.MyData['et'] = '3'
            self.MyData['ep'] = '2000,100'
            response3 = opener.open(self.Hgif + urllib.urlencode(self.MyData), timeout=timeout).info()
            pass
        except urllib2.HTTPError, ex:
            print ex.code
            pass
        except urllib2.URLError, ex:
            print ex.reason
            pass
        pass


if __name__ == "__main__":
    a = Baidu('id', 'http://www.xicidaili.com/nn/3447', 'http://www.xicidaili.com')
    a.run()
