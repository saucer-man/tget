#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright (c) saucerman (https://saucer-man.com)
See the file 'LICENSE' for copying permission
"""
import sys
import json
import base64
import config
from lib import data
import requests
import math

def check(email, key):  # verify email and key
    if email and key:
        auth_url = "https://fofa.so/api/v1/info/my?email={0}&key={1}".format(email, key)
        try:
            response = requests.get(auth_url)
            if response.status_code == 200:
                return True
        except Exception as e:
            data.logger.debug(e)
            return False
    return False


def handle_fofa(query: str, limit: int):
    email = config.fofa_email
    key = config.fofa_key
    try:
        msg = 'Trying to login with credentials in config file.'
        data.logger.info(msg)
        if check(email, key):
            pass
        else:
            raise Exception("Automatic authorization failed")   # will go to except block
    except Exception as e:
        data.logger.debug(e)
        msg = 'Automatic authorization failed.'
        data.logger.warn(msg)
        msg = 'Please input your FoFa Email and API Key below.'
        data.logger.warn(msg)
        email = input("Fofa Email: ").strip()
        key = input('Fofa API Key: ').strip()
        if not check(email, key):
            msg = 'Fofa API authorization failed, Please re-run it and enter a valid key.'
            data.logger.error(msg)
            sys.exit()

    query = base64.b64encode(query.encode('utf-8')).decode('utf-8')
    
    # 计算出第一页和最后一页，每页100个
    start_page = 1
    end_page = math.ceil(limit/100)
    res = set()
    for page in range(start_page, end_page+1):
        url = f"https://fofa.so/api/v1/search/all?email={email}&key={key}&qbase64={query}&page={page}&size=100"
        try:
            response = requests.get(url).text
            resp = json.loads(response)
            if not resp["error"]:
                for item in resp.get('results'):
                    res.add(item[0])
            else:
                data.logger.error(f"爬取第{page}页发生错误：{resp['errmsg']}")
                break
        except Exception as e:
            data.logger.error(f"爬取第{page}页发生错误：{e}")
            break
    return res
