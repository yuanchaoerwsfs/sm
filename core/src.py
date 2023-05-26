# coding:utf-8
# Author @sun
"""用户试图层"""

from interface import user_interface, bank_interface, shop_interface
from lib import common

logged_user = None
logged_admin = False


# 0、退出
def sign_out():
    print('\n感谢使用，欢迎下次光临！')
    exit()


# 1、注册功能
def register(is_admin=False):
    while True:
        # 1、让用户输入用户名和密码
        print('\n注册')
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()
        is_register = input('按任意键确认/n退出：').strip().lower()

        # 2、进行简单的逻辑判断
        # 2.1、判断用户是否想要退出
        if is_register == 'n':
            break

        # 2.2、判断两次输入的密码是否一致
        if password != re_password:
            print('\n两次输入的密码不一致！')
            continue

        import re
        # 2.3、校验用户名是否合法
        if not re.findall('^[a-zA-Z]\w{2,9}$', username):
            print('\n用户名长度必须为3-10个字符！\n只能由字母、数字、下划线组成，并只能以字母开头！')
            continue

        # 2.4、校验密码强度
        # if not re.findall('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,16}$', password):
        #     print('\n密码太弱，必须包含大写字母、小写字母以及数字，并且长度必须为8-16位！')
        #     continue

        # 3、做密码加密
        password = common.pwd_to_sha256(password)

        # 4、调用注册接口进行注册
        flag, msg = user_interface.register_interface(username, password, is_admin)
        print(msg)
        if flag:
            break


# 2、登录功能
def login():
    while True:
        print('\n登录')
        # 1、让用户输入用户名和密码
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        is_login = input('按任意键确认/n退出：').strip().lower()

        # 2、判断用户是否想要退出
        if is_login == 'n':
            break

        # 3、做密码加密
        password = common.pwd_to_sha256(password)

        # 4、调用接口层，把数据传给登录接口，让接口层调用数据层来校验用户名是否已存在
        flag, msg, is_admin = user_interface.login_interface(username, password)
        print(msg)
        if flag:
            global logged_user, logged_admin
            logged_user = username
            logged_admin = is_admin
            break


# 3、充值功能
@common.login_auth
def recharge(username=False):
    while True:
        print('\n充值')
        # 1、接收用户输入的充值金额
        amount = input('请输入充值金额：').strip()
        is_recharge = input('按任意键确认/n退出：').strip().lower()

        # 2、判断用户是否想要退出
        if is_recharge == 'n':
            break

        # 3、判断用户输入的是否是数字
        if not amount.isdigit():
            print('\n请输入正确的金额！')
            continue

        # 4、把amount转成int类型
        amount = int(amount)

        # 5、判断用户输入的是否是0
        if amount == 0:
            print('\n充值的金额不能为0！')
            continue

        # 6、调用充值接口进行充值
        if not username:
            username = logged_user
        flag, msg = bank_interface.recharge_interface(username, amount)
        print(msg)
        if flag:
            return True


# 4、转账功能
@common.login_auth
def transfer():
    while True:
        print('\n转账')
        # 1、接收用户输入的用户名和转账金额
        to_username = input('请输入转账目标的用户名：').strip()
        amount = input('请输入转账金额：').strip()
        is_transfer = input('按任意键确认/n退出：').strip().lower()

        # 2、判断用户是否想要退出
        if is_transfer == 'n':
            break

        # 3、判断用户输入的是否是数字
        if not amount.isdigit():
            print('\n请输入正确的金额！')
            continue

        # 4、把amount转成int类型
        amount = int(amount)

        # 5、判断用户输入的是否是0
        if amount == 0:
            print('\n转账的金额不能为0！')
            continue

        # 6、判断用户是否在给自己转账
        if logged_user == to_username:
            print('\n不能给自己转账！')
            continue

        # 7、调用转账接口
        flag, msg = bank_interface.transfer_interface(
            logged_user, to_username, amount
        )
        print(msg)
        if flag:
            break


# 5、提现功能
@common.login_auth
def withdraw():
    while True:
        print('\n提现')
        # 1、接收用户输入的提现金额
        amount = input('请输入提现金额：').strip()
        is_withdraw = input('按任意键确认/n退出：').strip().lower()

        # 2、判断用户是否想要退出
        if is_withdraw == 'n':
            break

        # 3、判断用户输入的是否是数字
        if not amount.isdigit():
            print('\n请输入正确的金额！')
            continue

        # 4、把amount转成int类型
        amount = int(amount)

        # 5、判断用户输入的是否小于500
        if amount < 500:
            print('\n提现的金额不能低于500！')
            continue

        # 6、调用提现接口
        flag, msg = bank_interface.withdraw_interface(logged_user, amount)
        print(msg)
        if flag:
            break


# 6、查看余额
@common.login_auth
def check_balance():
    print('\n查看余额')
    flag, msg = bank_interface.check_balance_interface(logged_user)
    print(msg)


# 7、查看流水
@common.login_auth
def check_flow():
    print('\n查看流水')
    flag, flow_list = bank_interface.check_flow_interface(logged_user)
    if not flow_list:
        print('\n当前用户没有流水！')
    for flow in flow_list:
        print(flow)


# 8、购物功能
@common.login_auth
def shopping():
    # 1、取商品菜单 进行循环展示
    goods = shop_interface.check_goods_interface('goods')
    if not goods:
        print('goods菜单配置文件不存在，请确认！')
        return
    while True:
        print(f'欢迎光临，购物管理商城！'.center(50, '*'))
        for index, good in enumerate(goods):
            print(f'{"序号":<15}{good.get("number"):<15}{good.get("name"):<15}{good.get("price")}')
    #2、选择商品序号，添加到购物车

# 9、查看购物车
@common.login_auth
def check_shopping_cart():
    pass


# 10、退出账号
@common.login_auth
def login_out():
    pass


# 11、管理员功能
@common.login_auth
def admin():
    from core import admin
    admin.main()


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
            if logged_admin:
                print(f'{num}:{func_dic[num][0]}')
            elif not num == '11':
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
