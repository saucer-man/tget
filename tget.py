import logging

from lib import data
from lib.log import init_log
import time
from lib.cmd import cmdparse
from lib.data import conf
from api import handle_fofa,handle_zoomeye

import os
def set_log(verbose):
    log_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, f'{time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())}.log')
    level=logging.INFO
    if verbose:
        level=logging.DEBUG
    data.logger = init_log(__name__, level, log_file)


if __name__ == "__main__":
    conf.update(cmdparse().__dict__)
    set_log(conf.verbose)
    res = set()
    if conf.api_name == "fofa":
        res = handle_fofa(conf.dork, conf.limit)
    elif conf.api_name =="zoomeye":
        res = handle_zoomeye(conf.dork, conf.limit)
    else:
        data.logger.error("illegal api type")
    # with open(conf.output, 'w') as f:
    #     for i in res:
    #         f.write(f"{i}\n")
    # data.logger.info(f"爬取到{len(res)}条数据，保存在{conf.output}中")


