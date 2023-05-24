# coding:utf-8
# Author @sun
"""银行相关接口"""
from db import db_handler
from conf import settings
from datetime import datetime


# 充值金额接口
def recharge_interface(amount, username):
    user_data = db_handler.select_data(username)
    user_data['balance'] += amount
    msg = f'{datetime.now().replace(microsecond=0)} 恭喜{username}成功充值{amount}元，当前账户余额为{user_data.get("balance")}元！'
    user_data['flow'].append(msg)
    db_handler.save(user_data)
    return True, msg


# 提现金额接口
def withdraw_interface(amount, username):
    user_data = db_handler.select_data(username)
    service_fee = int(amount * settings.RATE)
    if not (user_data.get('balance') + service_fee) > amount:
        msg = '账户余额不足！'
        return False, msg
    user_data['balance'] -= amount
    msg = f'{datetime.now().replace(microsecond=0)} 恭喜{username}成功提现{amount}元，手续费为{service_fee}元，当前账户剩余余额{user_data.get("balance")}元!'
    user_data['flow'].append(msg)
    db_handler.save(user_data)
    return True, msg


# 余额查询接口
def check_balance_interface(username):
    user_data = db_handler.select_data(username)
    msg = f'{username}账户当前余额为{user_data.get("balance")}元！'
    return True, msg


# 流水查询接口
def check_flow_interface(username):
    user_data = db_handler.select_data(username)
    return True,user_data.get('flow')

withdraw_interface(19,'sunqw')