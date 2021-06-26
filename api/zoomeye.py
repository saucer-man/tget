#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math
import zoomeye.sdk as zoomeye
import config
from lib import data


def handle_zoomeye(dork, limit=100, type="web") -> set:
    if len(config.zoomeye_apikey) < 36:
        data.logger.warn('illegal zoomeye_token in config file.')
        config.zoomeye_apikey = input("zoomeye_token: ").strip()
    zm = zoomeye.ZoomEye(api_key=config.zoomeye_apikey)
    try:
        data.logger.info(f"user info: {zm.resources_info()}")
    except:
        data.logger.info("login failed")
        sys.exit()
    result = set()
    end_page = math.ceil(limit / 20)
    for page in range(end_page):
        data.logger.info(f"正在爬取第{page}页")
        data_z = zm.dork_search(dork=dork, page=end_page, resource=type)
        if len(data_z) < 1:
            data.logger.debug(f"第{page}页没有数据，停止爬取")
            break
        for i in data_z:
            ip_str = i.get('ip')
            if 'portinfo' in i:
                ip_str = ip_str + ':' + str(i.get('portinfo').get('port'))
            result.add(ip_str)
    return result
