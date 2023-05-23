# coding:utf-8
# Author @sun
"""数据处理层"""
import os
import json

from conf import settings


# 查看用户是否存在
def select_data(username, data=True, is_user=True):
    user_path = os.path.join(settings.USER_DATA_DIR, f'{username}.json')
    if not os.path.exists(user_path):
        return
    if not data:
        return True
    with open(user_path, mode='rt', encoding='utf-8') as f:
        user_data = json.load(f)
        return user_data


def save(user_data):
    """

    :param user_data:
    :return:
    """
    user_path = os.path.join(settings.USER_DATA_DIR, f'{user_data.get("username")}.json')
    with open(user_path, mode='wt', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False)
