# -*- coding: utf-8 -*-
import requests
import json
from lxml import etree
import re 
import time
import BiliLogin

def 获取封面(avid):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    }
    url = 'http://search.bilibili.com/video?keyword='
    testurl = url + str(avid)
    html = requests.get(testurl,headers=header)
    img_url = re.findall(r'"pic":"(.*?)"', html.text)
    try:
        if img_url == []:
            print('err:'+"不存在De~")
        else:
            real_img_url = 'https:'+str(img_url[0].replace("u002F","").replace("\\","/"))
            return real_img_url
    except IndexError as e:
        print('err:'+str(e))
    finally:
        pass
def 获取弹幕(avid):
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

def 获取评论(avid):
    count=1
    url="http://api.bilibili.com/x/v2/reply?type=1&oid="
    html=url+avid+'&pn='
    fi=[]
    while(True):
        url=html+str(count)
        url=requests.get(url)
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
                    fi.append(hotMsg)
                    leng=len(cont['data']['hots'][i]['replies'])
                    for j in range(leng):
                        hotMsgRp=cont['data']['hots'][i]['replies'][j]['content']['message']
                        fi.append(hotMsgRp)
            except:
                pass
        if lengthRpy!=0:
            for i in range(lengthRpy):
                comMsg=cont['data']['replies'][i]['content']['message']
                fi.append(comMsg)
                if cont['data']['replies'][i]['replies']:
                    leng=len(cont['data']['replies'][i]['replies'])
                    for j in range(leng):
                        comMsgRp=cont['data']['replies'][i]['replies'][j]['content']['message']
                        fi.append(comMsgRp)
        else:
            break
        count += 1
    return fi

def 推荐():
    url=requests.get("http://api.bilibili.com/x/web-interface/dynamic/region?rid=1&jsonp=jsonp&_sw-precache=juoihjoi")
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
