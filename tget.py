import requests

from lib.log import set_log
import time
from lib.cmd import cmdparse
from lib.data import conf
logger = set_log(__name__)  # 日志方法调用

if __name__ == "__main__":
    logger.info("测试日志")
    conf.update(cmdparse().__dict__)
    print(conf)


