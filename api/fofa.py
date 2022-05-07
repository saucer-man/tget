#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json
import math
import sys

import requests

import config
from lib import data


def check(email, key):  # verify email and key
    if email and key:
        auth_url = "https://fofa.info/api/v1/info/my?email={0}&key={1}".format(email, key)
        try:
            response = requests.get(auth_url, timeout=5)
            if response.status_code == 200:
                return True
        except Exception as e:
            data.logger.debug(e)
            return False
    return False


def handle_fofa(query: str, limit: int):
    email = config.fofa_email
    key = config.fofa_key
    data.logger.info('Trying to login with credentials in config file.')
    if not check(email, key):
        data.logger.warn('Automatic authorization failed.')
        data.logger.warn('Please input your FoFa Email and API Key below.')
        email = input("Fofa Email: ").strip()
        key = input('Fofa API Key: ').strip()
        if not check(email, key):
            data.logger.error('Fofa API authorization failed, Please re-run it and enter a valid key.')
            sys.exit()
    data.logger.info("Login successfully")

    query = base64.b64encode(query.encode('utf-8')).decode('utf-8')
    # 计算出第一页和最后一页，每页100个
    start_page = 1
    end_page = math.ceil(limit / 100)
    res = set()
    for page in range(start_page, end_page + 1):
        data.logger.debug(f"爬取第{page}页...")
        url = f"https://fofa.info/api/v1/search/all?email={email}&key={key}&qbase64={query}&page={page}&size=100&fields=host,ip,protocol,port"
        try:
            response = requests.get(url).text
            resp = json.loads(response)
            if not resp["error"]:
                for item in resp.get('results'):
                    host = item[0]
                    protocol = item[2]
                    # 下面根据host,ip, protocal, port来组装，一般用host就够了，但是对于http/https还需要处理一下
                    if protocol == "https" or protocol == "http":
                        if not host.startswith("http"):
                            host = protocol +"://" + host
                    res.add(host)
            else:
                data.logger.error(f"爬取第{page}页发生错误：{resp['errmsg']}")
                break
        except Exception as e:
            data.logger.error(f"爬取第{page}页发生错误：{e}")
            break
    return res
