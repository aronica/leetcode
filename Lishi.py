# -*- coding: utf-8 -*-
# coding=utf-8
__author__ = 'fafu'
import sys
import urllib2
import string
import sys
import json

import os
from pyquery import PyQuery as pq
import lxml
import collections
from threading import Thread, Lock
import httplib
import time
import multiprocessing


host = "http://xy.eywedu.com/24/"

def calwer(queue):
    d = pq(url="http://xy.eywedu.com/24/")
    for i in d(".content tr td a"):
        queue.append(d(i).attr("href"))




def run_task(queue,queueout):
    while True:
        try:
            item = queue.popleft()
            if item is not None and item.find("/")>=0:
                d = pq(url=host+item)
                cata = item[0 : item.index("/")]
                for i in d(".content td a"):
                    queueout.append((host + cata+ '/' +d(i).attr("href"), d(i).text(),cata,d(i).attr('href')))
        except IndexError:
            break

def parse_content(queue):
    while True:
        try:
            item = queue.popleft()
            print item[2]+"\n"
            result = urllib2.urlopen(item[0]).read()
            result = result.replace("charset=gb2312","chartset=utf-8")
            result = result.decode("gbk","ignore")
            d = pq(result)
            for i in d('table'):
                table = d(i)
                if table.attr('width') != '94%':
                    continue
                td = table.find("tr").eq(2).find("td")
                td.children().eq(0).remove()
                td.children().eq(0).remove()
                if not os.path.exists(os.path.dirname("C:/Users/fafu/Desktop/lishi/"+item[2]+"/"+item[3])):
                    os.makedirs(os.path.dirname("C:/Users/fafu/Desktop/lishi/"+item[2]+"/"+item[3]))
                with open("C:/Users/fafu/Desktop/lishi/"+item[2]+"/"+item[3],"w") as f:
                    # print td
                    # print td.html()
                    if td.html() is not None:
                        print "item "+str(item)+" is Not None"
                        f.write(td.html())
                    else:
                        print "item "+str(item)+" is None"
        except IndexError as e:
            print "IndexError "+str(e.message)
            break
        except urllib2.HTTPError:
            print "HttpError "+str(e.message)
            continue
        finally:
            print "Finally"

def main(argv):
    print sys.getdefaultencoding()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    queue = collections.deque()
    queue2 = collections.deque()
    calwer(queue)
    run_task(queue,queue2)
    record = list()
    for i in range(4):
        proc = Thread(target=parse_content,args=(queue2,))
        proc.start()
        record.append(proc)

    for i in record:
        i.join()
    # parse_content(queue2)

    print "finish"

if __name__ == "__main__":
    main(sys.argv)