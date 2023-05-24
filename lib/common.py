# coding:utf-8
# Author @sun
"""公共方法"""
from core import src
#登陆装饰器
def login_auth(func):
    def warpper(*args, **kwargs):
        #使用装饰器对原函数进行功能扩展A
        if src.logged_user:
            ret = func(*args,**kwargs)
            return ret
        else:
            print('当前未登录用户，请进行账户登陆后操作！')
            src.login()
    return warpper


def pwd_to_sha256(password):
    import hashlib
    h1 = hashlib.sha512(password.encode('utf-8'))  #这货只管机密 没有解密，同数据加密结果一样，拿结果对比就完了
    h1.update('全世界最帅的男人！'.encode('gbk'))
    return h1.hexdigest()
