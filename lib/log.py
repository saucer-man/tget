import logging
import sys


def init_log(name, level, filename):
    '''
    初始化日志配置
    @param level:设置的日志级别。默认：DEBUG
    @param filename: 日志文件名。默认：当前目录下的pocoLog.txt，也可为绝对路径名
    '''

    logger = logging.getLogger(name)  # 日志
    logger.setLevel(level)
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
    streamHandler = logging.StreamHandler(sys.stderr)
    fileHandler = logging.FileHandler(filename=filename, mode='w', encoding='utf-8', delay=False)  # 输出到文本
    LOG_FORMAT1 = '[%(asctime)s] [%(levelname)s] %(message)s'
    LOG_FORMAT2 = '[%(asctime)s] [%(levelname)s] <%(name)s> <%(pathname)s]> (%(lineno)d) %(message)s'
    formatter1 = logging.Formatter(
        fmt=LOG_FORMAT1,
        datefmt='%Y-%m-%d  %H:%M:%S'
    )
    formatter2 = logging.Formatter(
        fmt=LOG_FORMAT2,
        datefmt='%Y-%m-%d  %H:%M:%S'
    )
    streamHandler.setFormatter(formatter1)
    fileHandler.setFormatter(formatter2)
    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)
    return logger
