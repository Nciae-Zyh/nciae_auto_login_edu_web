import urllib

import requests
import json
from urllib import request
import time

# 数据
data = {
    "R3": "1",
    "v6ip": "",
    "DDDDD": "用户名",
    "upass": "密码",
    "save_me": "1",
    "0MKKey": "%B5%C7%A1%A1%C2%BC"
}
# 访问头
header = {
    "Host": "10.99.92.3",
    "Connection": "keep-alive",
    "Content-Length": "78",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://10.99.92.3",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.63 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Referer": "http://10.99.92.3/0.htm",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-HK;q=0.8",
}

url = "http://10.99.92.3/0.htm"

file = open('c://autoEduLogin//user.txt', 'r')
js = file.read()
user = json.loads(js)
file.close()

data['DDDDD'] = user['username']
data['upass'] = user['password']


# 测试是否能访问登录页面
def test_WiFi():
    try:
        response = requests.post(url, data=data, headers=header).status_code
    except:
        print("请检查是否开启校园网WiFi自动登录！")
        return False
    return True


url1 = "http://www.baidu.com/"


def test_username_and_password():
    try:
        response = urllib.request.urlopen('https://www.baidu.com')
        response.read().decode('utf8')
    except:
        print('请检查账号密码是否输入正确！')
        return False
    return True


if test_WiFi() and test_username_and_password():
    print("登陆成功！感谢您的使用！——by小赵")

input("输入回车继续！")
