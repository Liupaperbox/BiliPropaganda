# BiliAutoPropaganda 哔哩哔哩自动宣传

## 通过匹配评论和弹幕来决定是否发送指定评论

要求：Python3

库:
argparse,lxml,re,time,json,requests,qrcode,matplotlib,pickle,os


[哔哩哔哩封面提取器](https://www.boxpaper.club/bilitools/)

初目的是宣传我做的封面提取器

Clone后可以直接运行Main.py,会出来扫码图片，使用哔哩哔哩手机客户端扫码获取Cookie并保存到cookie.pkl,

参数:

`-m 需要发送的消息，为字符串，换行用'\n'`

`-c 消息发送条件,为用','分割的任意字符`

实例:
`python Main.py -m https://www.boxpaper.club/bilitools/ -c 求封面,要封面`

截图

![1](/Screenshot/a1.png)

![2](/Screenshot/a3.png)

![3](/Screenshot/a2.png)

支持我的话，可以去我的[主页](https://www.boxpaper.club/)看看哦