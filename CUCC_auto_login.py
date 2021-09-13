import urllib

import requests
import json
from urllib import request
import time

import random
import string

import requests
import re
from urllib.parse import parse_qs
from urllib.parse import urlsplit

# 请求地址头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}
# 登录头
all_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-HK;q=0.8",
    "Referer": ""
}
# 登录数据
data = {
    'wlanuserip': 'id',
    'wlanacname': 'paun',
    'chal_id': '',
    'chal_vector': '',
    'auth_type': 'PAP',
    'seq_id': '',
    'req_id': '',
    'wlanacIp': 'wlanacIp',
    'ssid': '',
    'vlan': 'vlan',
    'mac': 'mac',
    'message': '',
    'bank_acct': '',
    'isCookies': '',
    'version': '0',
    'authkey': 'amnoon',
    'url': 'www.msftconnecttest.com/redirect',
    'usertime': '0',
    'listpasscode': '0',
    'listgetpass': '0',
    'getpasstype': '0',
    'randstr': '',
    'domain': '',
    'isRadiusProxy': 'false',
    'usertype': '0',
    'isHaveNotice': '0',
    'times': '12',
    'weizhi': '0',
    'smsid': '',
    'freeuser': '',
    'freepasswd': '',
    'listwxauth': '0',
    'templatetype': '1',
    'tname': '2',
    'logintype': '0',
    'act': '',
    'is189': 'false',
    'terminalType': '',
    'checkterminal': 'true',
    'portalpageid': '201',
    'listfreeauth': '0',
    'viewlogin': '1',
    'userid': '账号',
    'wisprpasswd': '',
    'twocode': '',
    'authGroupId': '',
    'alipayappid': '',
    'wlanstalocation': '',
    'wlanstamac': '',
    'wlanstaos': '',
    'wlanstahardtype': '',
    'smsoperatorsflat': '',
    'reason': '', 'res': '',
    'userurl': '',
    'challenge': '',
    'uamip': '',
    'uamport': '',
    'toqrcode': '',
    'isIOSPortal': 'false',
    'useridtemp': '账号',
    'passwd': '密码',
    'wxname': '',
    'wxuser': ''
}
# 验证方式数据
data2 = {
    "act": "check",
    "user_id": "账号"
}

file = open('c://autoEduLogin//user.txt', 'r')
js = file.read()
user = json.loads(js)
file.close()

static_url = 'http://www.msftconnecttest.com/redirect'
url = "http://10.99.92.3/0.htm"


def get_url():
    static_response = requests.get(static_url, headers=header)
    static_response_302_dict = dict(parse_qs(urlsplit(static_response.url).query))
    seeds = string.digits
    all_header['Referer'] = static_response.url
    data['wlanuserip'] = static_response_302_dict['clientip'][0]
    data['wlanacIp'] = static_response_302_dict['paip'][0]
    data['mac'] = static_response_302_dict['clientmac'][0]
    data['vlan'] = static_response_302_dict['vlan'][0]
    data['url'] = static_response_302_dict['iarmdst'][0]
    data['randstr'] = random.choices(seeds, k=4)
    data['userid'] = user['username']
    data['useridtemp'] = user['username']
    data2['user_id'] = user['username']
    data['passwd'] = user['password']
    return static_response.url


# 测试是否能访问登录页面
def test_WiFi():
    try:
        true_url = get_url()
        sub = '/'
        addr = [i.start() for i in re.finditer(sub, true_url)]
        # 登录验证
        requests.post(true_url[:addr[2] + 1] + 'questionnaireAction.do', data=data, headers=all_header)
        # 登录
        requests.post(true_url[:addr[2] + 1] + 'portalAuthAction.do', data=data,
                      headers=all_header).status_code
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
