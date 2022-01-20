# -*- coding: utf-8 -*-
# @Time : 2022/1/6 15:57
# @Author : zengxiaoyan
# @File : debugtalk.py

"""
自定义方法，yaml里调用的额外函数
"""
import hashlib
import random
import string
from pathlib import Path

import yaml


def gen_random_string(str_len,n):
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(str_len,n))

def gen_md5(*args):
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()


def read_yaml(yaml_name,key):
    with open(str(Path.cwd())+'\\'+yaml_name,mode='r',encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        print(value)
        return value[key]
# #
# if __name__ == '__main__':
#     print(read_yaml('extract.yaml','token'))