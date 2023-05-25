# coding: utf-8
# @Author:Sunqw
# 管理员功能

from interface import admin_interface
from core import src


# 管理员添加普通账户/管理员账户
def add_user():
    while True:
        is_admin = input('管理员用户为Y/普通用户为N：').strip().lower()
        is_add_user = input('缺人继续按任意键/n退出：').strip().lower()
        if is_add_user == 'n':
            break
        if is_admin != 'n' or is_admin != 'N':
            src.register(True)
            break
        else:
            src.register()
            break


# 管理员冻结/解冻账户
def lock_user():
    while True:
        lock_username = input('输入要冻结/解冻的账户').strip()
        is_lock_user = input('确认继续按任意键/n退出:').strip().lower()
        if is_lock_user == 'n':
            break
        flag, msg = admin_interface.lock_user_interface(lock_username)
        print(msg)
        if flag:
            break


# 管理员给用户充值
def recharge_to_user():
    while True:
        username = input('请输入要充值的账户：').strip()
        is_recharge_to_user = input('确认继续按任意键/n退出:').strip().lower()
        if is_recharge_to_user == 'n':
            break
        if src.recharge(username):
            break



func_dic = {
    '0': ("返回首页",),
    '1': ("添加普通账户/管理员账户", add_user),
    '2': ("冻结/解冻账户", lock_user),
    '3': ("给用户充值", recharge_to_user),
}


def main():
    while True:
        for i in func_dic:
            print(f'{i}:{func_dic[i][0]}')
        num = input('请输入选择的功能编号：').strip().lower()
        if num not in func_dic:
            print('无此功能序号，请重新输入！')
            continue
        if num == '0':
            break
        func_dic.get(num)[1]()
