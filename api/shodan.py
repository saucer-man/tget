#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import shodan
import config
from lib import data
import math


def handle_shodan(query, limit):
    res = set()
    api = shodan.Shodan(config.shodan_apikey)
    data.logger.info("Trying to login with credentials in config file")
    try:
        account_info = api.info()
    except shodan.exception.APIError as e:
        data.logger.warn('Automatic authorization failed.')
        data.logger.warn('Please input your Shodan API Key (https://account.shodan.io/).')
        api.api_key = input('[*] API KEY > ').strip()
        try:
            account_info = api.info()
        except shodan.exception.APIError:
            data.logger.error('Shodan API authorization failed, Please re-run it and enter a valid key.')
            sys.exit(-1)
    data.logger.info("Login successfully")
    data.logger.info(f"user info: {account_info}")
    data.logger.info(f"Available Shodan query credits: {account_info.get('query_credits')}")
    if account_info.get('query_credits') == 0:
        data.logger.warn("there is no api credits")
        return res
    # 计算出第一页和最后一页，每页100个
    start_page = 1
    end_page = math.ceil(limit / 100)

    for page in range(start_page, end_page):
        data.logger.debug(f"爬取第{page}页...")
        try:
            result = api.search(query=query, page=page)
            if not result.get('matches'):
                data.logger.debug(f"第{page}页没有数据，停止爬取")
                break
            for match in result.get('matches'):
                res.add(match.get('ip_str') + ':' + str(match.get('port')))
        except shodan.APIError as e:
            data.logger.error(f"爬取第{page}页发生错误：{e}")
            break
    return res
