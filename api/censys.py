#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

from censys.search import CensysHosts


import config
from lib import data


def handle_censys(query, limit):
    res = set()
    data.logger.info("Trying to login with credentials in config file")
    try:
        c = CensysHosts(api_id=config.censys_id,
                        api_secret=config.censys_secret)
        account_info = c.account()
    except Exception as e:
        print(e)
        data.logger.warn(
            "Automatic authorization failed.\n[*] Please input your censys API Key (https://censys.io/account/api).")
        config.censys_id = input('ID > ').strip()
        config.censys_secret = input('SECRET > ').strip()
        try:
            c = CensysHosts(api_id=config.censys_id,
                            api_secret=config.censys_secret)
            account_info = c.account()
        except:
            data.logger.error(
                'Censys API authorization failed, Please re-run it and enter a valid key.')
            sys.exit(-1)
    data.logger.info("Login successfully")
    data.logger.info(f"user info: {account_info}")

    pages = math.ceil(limit / 100)
    page_cu = 1
    try:
        # 这里只有ip，没有port。因为每个ip开放的port全在结果里面，没办法判断
        for page in c.search(query=query, per_page=100, pages=pages):
            data.logger.debug(f"爬取第{page_cu}页...")
            for data_c in page:
                res.add(data_c["ip"])
            page_cu += 1
    except Exception as e:
        data.logger.warn(f"出现错误: {e}")
        pass
    return res
