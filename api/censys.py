#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

from censys.search import CensysHosts
from censys.search import CensysIPv4

import config
from lib import data


def handle_censys(query, limit):
    res = set()
    data.logger.info("Trying to login with credentials in config file")
    try:
        c = CensysIPv4(api_id=config.censys_id, api_secret=config.censys_secret)
        account_info = c.account()
    except Exception as e:
        print(e)
        data.logger.warn(
            "Automatic authorization failed.\n[*] Please input your censys API Key (https://censys.io/account/api).")
        config.censys_id = input('ID > ').strip()
        config.censys_secret = input('SECRET > ').strip()
        try:
            c = CensysIPv4(api_id=config.censys_id, api_secret=config.censys_secret)
            account_info = c.account()
        except:
            data.logger.error('Censys API authorization failed, Please re-run it and enter a valid key.')
            sys.exit(-1)
    data.logger.info("Login successfully")
    data.logger.info(f"user info: {account_info}")
    h = CensysHosts(api_id=config.censys_id, api_secret=config.censys_secret)

    pages = math.ceil(limit / 100)
    page_cu = 1
    # 这里只有ip，没有port。因为每个ip开放的port全在结果里面，没办法判断
    for page in h.search(query=query, pages=pages):
        data.logger.debug(f"爬取第{page_cu}页...")
        for data_c in page:
            res.add(data_c["ip"])
        page_cu += 1
    return res
