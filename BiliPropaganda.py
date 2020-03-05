# -*- coding: utf-8 -*-
import requests
import json
from lxml import etree
import random
import string
import re 
import time
import BiliLogin
from tenacity import retry
@retry()
def 获取封面(av_num):
    header = {'Cookie':'','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    url = 'http://api.bilibili.com/x/web-interface/search/type?context=&search_type=video&page=1&order=&duration=&category_id=&tids_1=&tids_2=&__refresh__=true&highlight=1&single_column=0&jsonp=jsonp&keyword='
    testurl = url + str(av_num)
    data = json.loads(requests.get(testurl,headers=header).text)
    if data["code"]==0 and data["message"]=='0':
        if data["data"]["result"]!=[]:
            pic = data["data"]["result"][0]["pic"]
            return "https:" + pic
    return "还没有找到"
def 获取弹幕(avid):
    try:
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                }
        url = "http://api.bilibili.com/x/web-interface/view?aid="+avid
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            cid = json.loads(response.content.decode())["data"]["cid"]
            cid_url = "https://comment.bilibili.com/{}.xml".format(cid)
            result = requests.get(cid_url, headers=headers)
            comment_element = etree.HTML(result.content)
            d_list = comment_element.xpath("//d")
            ret=[]
            for d in d_list:
                ret.append(d.xpath("./text()")[0])
            return ret
    except:
        return []

def 获取评论(avid,ifrpid=False):
    count=1
    url="http://api.bilibili.com/x/v2/reply?type=1&oid="
    html=url+str(avid)+'&pn=1'
    fi=[]
    if ifrpid:
        li=[]
    A=True
    while A:
        url=html+str(count)
        A=False
        try:
            url=requests.get(url)
        except:
            A=True
        if url.status_code==200:
            cont=json.loads(url.text)
        else:
            break
        if cont['data']['replies']:
            lengthRpy = len(cont['data']['replies'])
        else:
            lengthRpy = 0
        if count==1:
            try:
                lengthHot=len(cont['data']['hots'])
                for i in range(lengthHot):
                    hotMsg=cont['data']['hots'][i]['content']['message']
                    if ifrpid:
                        hotMsgid=cont['data']['hots'][i]["rpid"]
                        li.append(hotMsgid)
                    fi.append(hotMsg)
                    leng=len(cont['data']['hots'][i]['replies'])
                    for j in range(leng):
                        hotMsgRp=cont['data']['hots'][i]['replies'][j]['content']['message']
                        if ifrpid:
                            hotMsgRpid=cont['data']['hots'][i]['replies'][j]["rpid"]
                            li.append(hotMsgRpid)
                        fi.append(hotMsgRp)
            except:
                pass
        if lengthRpy!=0:
            for i in range(lengthRpy):
                comMsg=cont['data']['replies'][i]['content']['message']
                if ifrpid:
                    comMsgid=cont['data']['replies'][i]["rpid"]
                    li.append(comMsgid)
                fi.append(comMsg)
                if cont['data']['replies'][i]['replies']:
                    leng=len(cont['data']['replies'][i]['replies'])
                    for j in range(leng):
                        comMsgRp=cont['data']['replies'][i]['replies'][j]['content']['message']
                        if ifrpid:
                            comMsgRpid=cont['data']['replies'][i]['replies'][j]["rpid"]
                            li.append(comMsgRpid)
                        fi.append(comMsgRp)
        else:
            break
        count += 1
    if ifrpid:
        return fi, li
    return fi

def 推荐():
    url=requests.get("http://api.bilibili.com/x/web-interface/dynamic/region?rid=1&jsonp=jsonp&_sw-precache="+"".join(random.sample(string.ascii_letters + string.digits, 8)))
    if url.status_code==200:
        cont=json.loads(url.text)
        cont=cont["data"]["archives"]
        result=[]
        for i in cont:
            result.append(str(i["aid"]))
        return result

def 发送评论(aid,message):
    cookie=BiliLogin.main()
    data={
            "oid":aid,
            "type":1,
            "message":message,
            "plat":1,
            "jsonp":"jsonp",
            "csrf":cookie["bili_jct"]
            }
    r = requests.post("http://api.bilibili.com/x/v2/reply/add",data=data,cookies=cookie)
    if r.status_code==200:
        cont=json.loads(r.text)
        return cont
def 举报(aid,rpid):
    cookie=BiliLogin.main()
    data={
            "oid":aid,
            "type": 1,
            "rpid": rpid,
            "reason": 1,
            "content":"",
            "jsonp":"jsonp",
            "csrf":cookie["bili_jct"]
            }
    r = requests.post("https://api.bilibili.com/x/v2/reply/report",data=data,cookies=cookie)
    if r.status_code==200:
        cont=json.loads(r.text)
        return cont
