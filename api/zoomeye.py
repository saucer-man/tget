#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright (c) saucerman (https://saucer-man.com)
See the file 'LICENSE' for copying permission
"""
import zoomeye.sdk as zoomeye
import config
from lib import data

def handle_zoomeye(query, limit=100, type="web") -> set:
    if len(config.zoomeye_apikey) < 36:
        data.logger.warn('illegal zoomeye_token in config file.')
        config.zoomeye_apikey = input("zoomeye_token: ").strip()
    zm = zoomeye.ZoomEye(api_key=config.zoomeye_apikey)
    print(zm.resources_info())
    return set()
