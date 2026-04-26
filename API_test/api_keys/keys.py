# -*- coding:utf-8 -*-
# @FileName  :keys.py
# @Time      :2024/5/7 15:54
# @Author    :Daisy
# @Brief Introduction    : 接口关键字驱动类，封装常用接口测试方法

import requests

from API_test.conf import set_conf


class ApiKeys:
    # get
    def do_get(self, path=None, headers=None, params=None, **kwargs):
        # url的拼接
        url = self.set_url(path)
        headers = self.set_headers(headers)
        return requests.get(url=url, headers=headers ,params=params, **kwargs)

    # post:如果需要传递json格式的内容，需要进行二次参数处理
    def do_post(self, path=None, headers=None, data=None, json=1, **kwargs):
        # url的拼接
        url = self.set_url(path)
        headers = self.set_headers(headers)
        if json:
            respones = requests.post(url=url, headers=headers, json=data, **kwargs)
        else:
            respones = requests.post(url=url, headers=headers, data=data, **kwargs)
        return respones

    # 拼接url
    def set_url(self, path=None):
        base_url = set_conf.read('servers', 'UAT')
        if path:
            url = base_url + path
        return url

    # headers拼接
    def set_headers(self, headers=None):
        # 定义通用header基础信息，简化请求参数定义和设置、测试用例和数据内容
        base_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": "RANDOM_CODE=${RANDOM_CODE}"  # 从环境变量或配置文件读取
        }
        # 如果有新的信息加入，则补充header内容
        if headers:
            base_headers.update(headers)
        return base_headers