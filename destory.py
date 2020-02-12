# -*- coding: utf-8 -*-
"""
举报者
"""

from BiliPropaganda import *
import re
import time

def 尝试举报(aid,rpid):
    发送结果 = 举报(aid,rpid)
    if 发送结果["code"] == 0:
        print("发送成功！")
        time.sleep(10)
    else:
        print("发送失败！")
        print(发送结果["message"])
        if "data" in 发送结果:
            print(发送结果["data"])
            if "ttl" in 发送结果["data"]:
                print(发送结果["data"]["ttl"])
                time.sleep(发送结果["data"]["ttl"])
                尝试举报(aid,rpid)
def Main(匹配):
    alist = 推荐()
    for i in alist:
        评论,评论id = 获取评论(i,True)
        for a in range(len(评论)):
            for v in 匹配:
                result = re.search(v,评论[a])
                if result:
                    
                    print(评论[a])
                    尝试举报(i,评论id[a])
                    
while True:
    Main(["m.baidu.com/from=1001703","galmoe.com","b.qiuyeye.cn","u.nu/tzp3","irbq.top"])