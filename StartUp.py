import ctypes
import os

import requests
import sys
import json
import easygui as ui

# 数据

user = {
    "username": "",
    "password": ""
}


# 获取管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# 以管理员权限运行创建计划任务
if is_admin():
    Msg = '欢迎使用北华航天工业学院连通网络自动登录系统'
    Tittle = '自动登录系统'
    Fields = ['学号', '密码']
    ret = ui.multpasswordbox(Msg, Tittle, Fields)
    user['username'] = ret[0]
    user['password'] = ret[1]

    if not os.path.isdir('c://autoEduLogin'):
        os.mkdir('c://autoEduLogin')

    js = json.dumps(user)
    file = open('c://autoEduLogin//user.txt', 'w')
    file.write(js)
    file.close()

    CT = ('中国电信', '中国连通')
    while 1:
        ret = ui.choicebox(msg='', title='', choices=CT)
        if ret == CT[0]:
            str_in = 'schtasks /create /tn 开机自动登录电信校园网 /tr ' + os.getcwd() + '\\CTCC_auto_login.exe' + ' /sc onlogon'
            break
        elif ret == CT[1]:
            str_in = 'schtasks /create /tn 开机自动登录连通校园网 /tr ' + os.getcwd() + '\\CUCC_auto_login.exe' + ' /sc onlogon'
            break
        else:
            print('请选择您的运营商！')
    p = os.system(str_in)
    input('输入回车继续！')
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)
