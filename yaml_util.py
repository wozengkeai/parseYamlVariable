# -*- coding: utf-8 -*-
# @Time : 2022/1/5 11:30
# @Author : zengxiaoyan
# @File : yaml_util.py
"""
封装传递yaml文件的方法
"""

# import os

import json


import yaml
from pathlib import Path
# from ReadYamlRender import ReadYamlRender
from parse import ReadYamlRender

#读取yml用例文件
def read_testcase_yaml(yaml_name):
    """
    读取yml文件，对yaml反序列化，就是把yaml格式转化为dict格式
    :return:
    """
    with open(str(Path.cwd())+'\\'+yaml_name,mode='r',encoding='utf-8') as f:
        # value = yaml.load(f,Loader=yaml.FullLoader)
        value = f.read()
        value = ReadYamlRender().content_function(value)
        # value = yaml.load(value, Loader=yaml.FullLoader)
        return value







if __name__ == '__main__':
    read_testcase_yaml('anonymousLogin.yml')
    # read_yaml('\\extract.yaml','token')