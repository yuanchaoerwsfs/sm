# coding:utf-8
# Author @sun
"""购物相关接口"""

from db import db_handler


def check_goods_interface(goods_filename):
    goods = db_handler.select_data(goods_filename)
    if not goods:
        # msg = f'无{goods_filename}菜单，请确认后重新输入！'
        return False
    return goods
