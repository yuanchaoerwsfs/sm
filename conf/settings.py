# coding:utf-8
# Author @sun
"""配置信息"""

import configparser
import os


# 获取USER_DATA路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, 'settings.cfg')
config = configparser.ConfigParser()  # 创建对象
config.read(CONFIG_PATH, encoding='utf-8-sig')  # 指定路径文件
USER_DATA_DIR = config.get('path', 'USER_DATA_DIR')  # 读取路径中数据
if not os.path.isdir(USER_DATA_DIR):
    USER_DATA_DIR = os.path.join(BASE_DIR, 'db', 'user_data')
