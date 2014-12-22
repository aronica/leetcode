# -*- coding: utf-8 -*-
# coding=utf-8
__author__ = 'fafu'
import sys
import urllib2
import string
import sys
import json

from pyquery import PyQuery as pq
import lxml


from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []
        self.current = None

    def handle_starttag(self,tag,attrs):
        if tag == "a":
            for name,value in attrs:
                if value is None:
                    break
                idx = string.find(value,"/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/0")
                md_idx = string.find(value,".md")
                if name == "href" and idx >=0 :
                    self.current = {}
                    self.current['id'] = value[string.rfind(value,'/')+1:string.rfind(value,".md")]
                    self.current['url'] = value

    def handle_data(self, data):
        if self.current is not None:

            print data,isinstance(data,unicode)
            self.current['title'] = data
            self.data.append(self.current)
            self.current = None


class DetailHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.found = False
        self.data = None

    def handle_starttag(self,tag,attrs):
        if tag=="pre":
            self.found = True
    def handle_data(self,data):
        if self.found:
            self.data = data
            self.found = False
            print data

class FrontHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.found = False
        self.part = []
        self.tasklist = 0

    def handle_starttag(self,tag,attrs):
        if tag=="a":
            for key,value in attrs:
                if key=="name" and string.rstrip(value)=="user-content-html" and len(attrs) == 2:
                    self.html_found = True


def getFront():
    d = pq(url="https://github.com/markyun/My-blog/tree/master/Front-end-Developer-Questions/Questions-and-Answers#other")
    data = []
    for i in d("ul.task-list"):
        for j in d(i).children():
            item = dict()
            item["key"] = d(j).find("p").text().encode("utf-8")
            item["value"] = d(j).find("pre").text().encode("utf-8")
            # print "%s" % str(item)
            data.append(item)
    print str(data).decode("utf-8")
    with open("C:/Users/fafu/git/app/www/js/front.js",'w') as f:
        f.write("var fqs = ")
        f.write(json.dumps(data,  ensure_ascii=False))


def main(argv):
    if True:
        getFront()
        return 0

    print sys.getdefaultencoding()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print sys.getdefaultencoding()
    response = urllib2.urlopen("https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/Readme.md");
    parser = MyHTMLParser()
    # parser.handle_starttag('a',)
    parser.feed(response.read())

    print parser.data

    for i in parser.data:
        res = urllib2.urlopen("https://raw.githubusercontent.com"+string.replace(i["url"],"/blob",""))
        f = open("C:/Users/fafu/git/app/www/js/"+i["id"]+".json",'w')
        f.write(res.read())
        f.close()
        ia = string.split(i["id"],".")
        del i["url"]
        for idx,j in enumerate(ia):
            if j[0] == '0':
                ia[idx] = j[1:]
        i["id"] = string.join(ia,".")
    print  json.dumps(parser.data, encoding="UTF-8", ensure_ascii=False)

    f = open("C:/Users/fafu/git/app/www/js/package.json",'wb')
    f.write(json.dumps(parser.data, encoding="UTF-8", ensure_ascii=False))
    f.close()

if __name__ == "__main__":
    main(sys.argv)