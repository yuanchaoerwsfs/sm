# coding:utf-8
# Author @sun
"""管理员相关接口"""

from db import db_handler


def lock_user_interface(username):
    user_data = db_handler.select_data(username)
    if not user_data:
        msg = f'{username}账户不存在！'
        return False, msg
    if user_data.get('locked'):
        user_data['locked'] = False
        msg = f'用户{username}已解冻！'
        return True, msg
    else:
        user_data['locked'] = True
        msg = f'用户{username}已冻结！'
        return True, msg
