#!/usr/bin/env python
# coding=utf-8

"""
@Author  :   shumeng.ren
 
@License :   (C) Copyright from 2018, shumeng.ren
 
@Email :   rensm@inke.cn
 
@Software:   PyCharm
 
@File    :   me.py
 
@Time    :   2018-06-12 下午5:47
 
@Desc    : 
 
"""

import json
import urllib2

import lxml.etree as etree
import time

# 默认每次取200个
WHITE_LEN_ON_REQUEST = 200


def _get_score2(v):
    url = "http://life.httpcn.com/cp_jx.asp?isbz=0&pro=%B6%F5&cpzm=C&word=08S06&data_type=0&year=1980&month=6&day=13&hour=13&minute=10&pid=&cid=&name=&sex=1&act=submit"
    temp_url = url.replace("08S06", v)
    # print "temp_url:", temp_url
    response = urllib2.urlopen(temp_url)
    data = response.read()
    # print html

    html = data.decode('UTF-8', 'ignore')
    page = etree.HTML(html.lower())
    hrefnames = page.xpath('/ html / body / div[8] / div[1] / div[2] / div[6] / div[2] / font[2]/text()')

    return hrefnames[0]


def _get_score(v):
    url = "http://chepai.1518.com/chepai.php?st=9&v=1&chepai1=%B6%F5&chepai2=C&word=08S06&submit="
    temp_url = url.replace("08S06", v)
    # print "temp_url:", temp_url
    response = urllib2.urlopen(temp_url)
    data = response.read()
    # print html

    html = data.decode('UTF-8', 'ignore')
    page = etree.HTML(html.lower())
    hrefnames = page.xpath('//*[@id="main"]/div[2]/dl[1]/dd/div/font/u/b/text()')

    return hrefnames[0]


def get_data():
    url = "http://hb.122.gov.cn/m/mvehxh/getTfhdList?page=10&glbm=420300000400&hpzl=02&type=0&startTime=2018-01-01&endTime=2018-06-13"

    def do_get_data(page):
        import urllib2
        response = urllib2.urlopen(url.replace("page=10", page))
        text = response.read()
        return [item["subhd"] for item in json.loads(text)["data"]["list"]["content"]]

    res = []
    for i in range(20):
        temp = do_get_data("page={0}".format(1))
        print "temp:", temp
        res += temp

    print len(res)

    for item in res:
        "C18E00 ~ C18E99"
        temp = item.split("~")[0].strip()[1:-2]
        for r in range(100):
            v = "%s%02d" % (temp, r)
            # print "v:", v
            time.sleep(0.005)
            score = _get_score(v.upper())
            score2 = _get_score2(v.upper())
            if (int(score.strip()) >= 95 and int(score2.strip()) >= 95):
                print "鄂C{0}:{1}:{2}".format(v, score, score2)


    temp_list = ["08c06",
                 "08S06",
                 "25F11",
                 "25A11",
                 "05C11",
                 "25F11",
                 ]


    # digit = ["11"]
    # string = "ABCDFGJ"
    # digit = ["05"]
    # string = "ABCDPX"
    #
    # temp_least_res = []
    # for c in string:
    #     for d1 in digit:
    #         for d2 in range(100):
    #
    #             v = "%s%s%02d" % (d1, c, d2)
    #             score = _get_score(v.upper())
    #             score2 = _get_score2(v.upper())
    #             if (int(score.strip()) >= 95 and int(score2.strip()) >= 95):
    #                 temp_v = "鄂C{0}:{1}:{2}".format(v, score, score2)
    #                 temp_least_res.append((temp_v, (int(score) + int(score2)) / 2.0))
    #                 # print "鄂C{0}:{1}".format(v, score)
    #
    # for v in sorted(temp_least_res, key=lambda x:float(x[1]), reverse=True):
    #     print v[0]

def solve_main():
    get_data()



if __name__ == '__main__':
    solve_main()
