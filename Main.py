from BiliPropaganda import *
import BiliLogin
import argparse

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

BiliLogin.main()
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--message", help="需要发送的消息，为字符串，换行用'\\n'")
parser.add_argument("-c", "--condition", help="消息发送条件,为用','分割的任意字符")
args = parser.parse_args()
if args.message:
    message = args.message
else:
    exit()
if args.condition:
    condition = args.condition
else:
    exit()
if not 'condition' in locals().keys():
    while True:
        print("start...")
        Main("我自己做的封面提取\nhttp://t.cn/Ai8KbsTs\n各位可以支持一下吗(>▽<)\n这个视频的封面%s",["求封面","要封面"])
        time.sleep(30)
else:
    condition = condition.split(",")
    while True:
        print("start...")
        Main(message,condition)
        time.sleep(30)