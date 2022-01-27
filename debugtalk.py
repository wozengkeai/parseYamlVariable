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
from typing import Text, List, Dict
import yaml
import csv

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

def read_csv_file(csv_file: Text) -> List:
    csv_content_list = []

    with open(csv_file, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_content_list.append(row)

    return csv_content_list
# #
if __name__ == '__main__':
    print(read_csv_file('logindata.csv'))