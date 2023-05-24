# coding:utf-8
# Author @sun
"""银行相关接口"""
from db import db_handler
from conf import settings


def recharge_interface(amount, username):
    user_data = db_handler.select_data(username)
    user_data['balance'] += amount
    db_handler.save(user_data)
    msg = f'恭喜{username}成功充值{amount}元，当前账户余额为{user_data.get("balance")}元！'
    return True, msg


def withdraw_interface(amount, username):
    user_data = db_handler.select_data(username)
    service_fee = amount * settings.RATE
    if not (user_data.get('balance') + service_fee) > amount:
        msg = '账户余额不足！'
        return False, msg
    user_data['balance'] -= amount
    db_handler.save(user_data)
    msg = f'恭喜{username}成功提现{amount}元，手续费为{service_fee}元，当前账户剩余余额{user_data.get("balance")}元!'
    return True, msg


def check_balance_interface(username):
    user_data = db_handler.select_data(username)
    msg = f'{username}账户当前余额为{user_data.get("balance")}元！'
    return True, msg
