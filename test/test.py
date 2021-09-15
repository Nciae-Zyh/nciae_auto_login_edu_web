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
# if is_admin():
#     str_in = 'schtasks /create /tn 开机自动登录电信校园网 /tr ' + os.getcwd() + '\\CTCC_auto_login.exe' + ' /sc onlogon /delay 0000:05'
#     os.system(str_in)
#     # print(p)
#     # input()
# else:
#     if sys.version_info[0] == 3:
#         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#     else:
#         ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)

# for i in range(12000):
#     print(i)
#     if i == 20:
#         ui.msgbox(msg='初始化成功！', title='正经的提示', ok_button='好的！')
print(ui.ccbox(msg='计划任务添加失败！请重试！', title='不正经的，不应该出现的提示', choices=('True', 'False')))