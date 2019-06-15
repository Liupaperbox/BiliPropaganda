from BiliPropaganda import *
import BiliLogin

def Main(发送,匹配):
    alist = 推荐()
    for i in alist:
        评论 = 获取评论(i)
        弹幕 = 获取弹幕(i)
        所有 = 评论 + 弹幕
        是否找到 = False
        for a in 所有:
            for v in 匹配:
                result = re.search(v,a)
                if result:
                    print(a)
                    是否找到 = True
        if 是否找到:
            发送结果 = 发送评论(i,发送)
            if 发送结果["code"] == 0:
                print("发送成功！")
            else:
                print("发送失败！")
                print(发送结果["message"])
            print(i)

BiliLogin.main()
while True:
    Main("https://www.boxpaper.club/bilitools/",["求封面","要封面"])
    time.sleep(30)