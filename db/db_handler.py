# coding:utf-8
# Author @sun
"""
数据处理层
"""
import json
import os
from conf import settings


# 查询数据
def select_data(username, data=True, is_user=True):
    if is_user:
        # 1、接收逻辑接口层传过来的username，并拼接处用户名.json的路径
        user_path = os.path.join(
            settings.USER_DATA_DIR, f'{username}.json'
        )
    else:
        user_path = os.path.join(
            settings.GOODS_DATA_DIR, f'{username}.json'
        )
    # 2、判断用户名.json是否存在
    if not os.path.exists(user_path):
        return
    # 3、判断接口层是否需要用户数据，不需要则返回True
    if not data:
        return True
    # 4、需要，则读取用户数据，并返回用户数据
    with open(user_path, mode='rt', encoding='utf-8-sig') as f:
        user_data = json.load(f)
        return user_data


# 保存数据
def save(user_data):
    # 1、接收逻辑接口层传过来的user_data，并拼接处用户名.json的路径
    username = user_data.get('username')
    user_path = os.path.join(
        settings.USER_DATA_DIR, f'{username}.json'
    )

    # 2、保存用户数据
    with open(user_path, mode='wt', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False)


