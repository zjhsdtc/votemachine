#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import json

def post(url, data, proxy):
    try:
        print 'http://'+proxy
        proxy_support = urllib2.ProxyHandler({'http': 'http://'+str(proxy)})
        #proxy_support = urllib2.ProxyHandler({'http': 'http://42.121.28.111:3128'})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        content = urllib2.urlopen('http://babyshow.telltour.com/site/xxsd/').read()
        req = urllib2.Request(url)
        data = urllib.urlencode(data)
        #enable cookie
        #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, data)
        return response.read()
    except:
        return "cleantha"

def getproxy():
    proxylist = []
    file = open('proxylist', 'r')
    for line in file.readlines():
        if 'HTTP' in line:
            proxyitem = str(line.split('HTTP')[0].strip())
            proxylist.append(proxyitem)
    file.close()
    return proxylist

def main():
    proxylist = getproxy()
    posturl = "http://babyshow.telltour.com/admin/plugin/tomms/candidate/?m=app&c=candidateManager&a=getVote"
    data = {'id': 6}
    for proxy in proxylist:
        print post(posturl, data, proxy)
    #posturl = "http://babyshow.telltour.com/admin/plugin/tomms/candidate/?m=app&c=candidateManager&a=getCandidateVotes"
    #data = {}
    #print post(posturl, data)

if __name__ == '__main__':
    main()
