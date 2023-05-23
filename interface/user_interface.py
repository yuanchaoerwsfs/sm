# coding:utf-8
# Author @sun
"""用户相关接口"""
from db import db_handler


def register_interface(username, password, is_admin=False, balance=0):
    """

    :param username:
    :param password:
    :param is_admin:
    :param balance:
    :return:
    """
    if db_handler.select_data(username, False):
        return False, '\n用户名已存在！'
    # 2、组织用户数据字典
    user_data = {
        'username': username,
        'password': password,
        'balance': balance,
        'shopping_cart': {},
        'flow': [],
        'is_admin': is_admin,
        'locked': False,
    }
    db_handler.save(user_data)
    msg = f'用户：{username} 注册成功'
    return True, msg
