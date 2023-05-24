"""
用户相关接口
"""

from db import db_handler
from lib import common


# logger = common.get_logger('user')


# 注册接口
def register_interface(username, password, is_admin=False, balance=0):
    '''
    注册接口
    :param username: 用户名 str
    :param password: 密码 str
    :param is_admin: 是否是管理员，boolean
    :param balance: 初始余额 int
    :return: (boolean, str)
    '''
    # 1、调用接口层的查询功能，查询用户名是否已存在
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
    # 3、调用数据处理层，保存用户数据
    db_handler.save(user_data)
    msg = f'用户：{username} 注册成功！'
    # logger.info(msg)
    return True, msg


# 登录接口
def login_interface(username, password):
    # 1、调用数据处理层，查看用户是否存在
    user_data = db_handler.select_data(username)
    if not user_data:
        return False, f'\n用户：{username} 不存在，请重新输入！', False

    # 2、用户存在，继续校验密码
    if not password == user_data.get('password'):
        return False, '\n用户名或密码错误！', False

    # 3、密码正确，校验用户是否被冻结
    if user_data.get('locked'):
        return False, f'\n用户：{username} 已被冻结！', False
    msg = f'用户：{username} 登录成功！'
    # logger.info(msg)
    return True, msg, user_data.get('is_admin')
