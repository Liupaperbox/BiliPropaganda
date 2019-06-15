# -*- coding: utf-8 -*-
import requests
import qrcode
import matplotlib.pyplot as plt
import time
import json
import pickle
import os

class BilibiliLogin():
    def __init__(self):
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/63.0.3239.132 Safari/537.36',
                }
    def getLogin(self):
        r = requests.get('https://passport.bilibili.com/qrcode/getLoginUrl',headers=self.headers)
        j = json.loads(r.text)
        if j["code"]==0:
            img = qrcode.make(j["data"]["url"])
            plt.imshow(img)
            plt.show()
            return j["code"],j["data"]["oauthKey"]
        else:
            return j["code"],""
    def getInfo(self,oauthKey):
        r = requests.post('https://passport.bilibili.com/qrcode/getLoginInfo',headers=self.headers,data = {'oauthKey':oauthKey,'gourl':'https://www.bilibili.com/'})
        j = json.loads(r.text)
        return j,r.cookies
    def pickla(self,file,things):
        if os.path.exists(file):
            with open(file,'rb') as f:
                data = pickle.load(f)
            return data
        else:
            if things:
                with open(file,'wb') as f:
                    pickle.dump(things,f)
                return True
            else:
                return False
def main():
    loga=BilibiliLogin()
    pick = loga.pickla("cookie.pkl",False)
    if pick:
        return pick
    else:
        code,key = loga.getLogin()
        if code==0:
            while(1):
                info,cookies=loga.getInfo(key)
                if info["status"]==True:
                    print("Done!")
                    loga.pickla("cookie.pkl",cookies)
                    return cookies
                    break
                elif info["data"]==-5:
                    print("already scan(>_<)")
                else:
                    print("wating...")
                    pass
                time.sleep(5)