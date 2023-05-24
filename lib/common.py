# coding:utf-8
# Author @sun
"""公共方法"""


def pwd_to_sha256(password):
    import hashlib
    h1 = hashlib.sha512(password.encode('utf-8'))  #这货只管机密 没有解密，同数据加密结果一样，拿结果对比就完了
    h1.update('全世界最帅的男人！'.encode('gbk'))
    return h1.hexdigest()
