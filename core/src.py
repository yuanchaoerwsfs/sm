# coding:utf-8
# Author @sun
"""用户试图层"""

import re

from interface import user_interface


# 0、退出
def sign_out():
    print('后会有期，退出成功！')
    exit()


# 1、注册功能
def register():
    while True:
        username = input('请输入账号：'.center(20, '*').strip())
        password = input('请输入密码：'.center(20, '*').strip())
        re_password = input('请再次输入密码：'.center(20, '*').strip())
        is_register = input('请输入任意键/n退出'.center(20, '*').strip().lower())
        if is_register == 'n':
            break
        if password != re_password:
            print('两次输入的密码不一致，请重新输入')
            continue
        if not re.findall('^[a-zA-z0-9-_]{2,9}$', username):
            print('\n用户名长度必须为3-10个字符！\n只能由字母、数字、下划线组成，并只能以字母开头！')
            continue
        if not re.findall('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,16}$', password):
            print('\n密码太弱，必须包含大写字母、小写字母以及数字，并且长度必须为8-16位！')
            continue
        flag, msg = user_interface.register_interface(username, password)
        print(msg)
        if flag:
            break
# 2、登录功能
def login():
    pass


# 3、充值功能
def recharge():
    pass


# 4、转账功能
def transfer():
    pass


# 5、提现功能
def withdraw():
    pass


# 6、查看余额
def check_balance():
    pass


# 7、查看流水
def check_flow():
    pass


# 8、购物功能
def shopping():
    pass


# 9、查看购物车
def check_shopping_cart():
    pass


# 10、退出账号
def login_out():
    pass


# 11、管理员功能
def admin():
    pass


# 函数字典
func_dic = {
    '0': ('退出', sign_out),
    '1': ('注册功能', register),
    '2': ('登录功能', login),
    '3': ('充值功能', recharge),
    '4': ('转账功能', transfer),
    '5': ('提现功能', withdraw),
    '6': ('查看余额', check_balance),
    '7': ('查看流水', check_flow),
    '8': ('购物功能', shopping),
    '9': ('查看购物车', check_shopping_cart),
    '10': ('退出账号', login_out),
    '11': ('管理员功能', admin),
}


def main():
    while True:
        print('欢迎访问购物管理系统'.center(20, '*'))
        for num in func_dic:
            print(f'{num}:{func_dic[num][0]}')
        num1 = input('请输入对应项目序号：').strip()
        if num1 not in func_dic:
            print('*' * 20)
            print('*无此功能，请重新输入！*')
            print('*' * 20)
            continue
        print('*' * 20)
        func_dic[num1][1]()
        print('*' * 20)
