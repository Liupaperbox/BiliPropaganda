from BiliPropaganda import *
import BiliLogin

def Main(发送,匹配):
    alist = 推荐()
    for i in alist:
        评论 = 获取评论(i)
        弹幕 = 获取弹幕(i)
        所有 = 评论 + 弹幕
        是否找到 = 0
        for a in 所有:
            for v in 匹配:
                result = re.search(v,a)
                if result:
                    print(a)
                    是否找到 += 1
        if 是否找到>5:
            封面 = 获取封面(i)
            发送结果 = 发送评论(i,发送 % 封面)
            if 发送结果["code"] == 0:
                print("发送成功！")
            else:
                print("发送失败！")
                print(发送结果["message"])
            print(i)
comments=获取评论(91572143)
BiliLogin.main()
while False:
    print("start...")
    Main("我自己做的封面提取\nhttps://u.nu/zm8p\n各位可以支持一下吗(>▽<)\n如果想要找到P站原图，请先在https://saucenao.com/搜索P站Id,然后去我做的P站图片获取上下载https://www.boxpaper.club/PixivUMP/\n这个视频的封面%s",["求封面","要封面"])
    time.sleep(5)
    
