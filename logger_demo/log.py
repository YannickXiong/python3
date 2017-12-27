# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 20:16
# @Author  : Yannick
# @File    : log.py


import yaml
import logging
import logging.config

__config__ = "log_demo.conf"


def get_log_level(config_file):

    # 没有必要，不配置就给个默认值就OK
    # try:
    #     with open(config_file) as fp:
    #         config = yaml.load(fp)
    #
    #     if config.__contains__("logLevel"):
    #         _level = config["logLevel"].upper()
    #     else:
    #         raise KeyError("configure item <logLevel> doesn't exist in the the configuration file: "
    #                        + __config__ + "!")
    # finally:
    #     return _level
    with open(config_file) as fp:
        config = yaml.load(fp)

        if config.__contains__("logLevel"):
            return config["logLevel"]

        return "NOTSET"


class Log:

    def __init__(self):
        # 如果放在这里，所有子类都会隐式调用get_log_level，当有异常时，同一异常会抛出多次打印
        # self.log_level = get_log_level("conf.yaml")
        self.log_conf_file = __config__


class LogDebug(Log):

    def __init__(self):
        super(LogDebug, self).__init__()

    def get_logger(self):
        logging.config.fileConfig(self.log_conf_file)
        return logging.getLogger("logDebug")


class LogWarn(Log):

    def __init__(self):
        super(LogWarn, self).__init__()

    def get_logger(self):
        logging.config.fileConfig(self.log_conf_file)
        return logging.getLogger("logWarn")


class LogError(Log):

    def __init__(self):
        super(LogError, self).__init__()

    def get_logger(self):
        logging.config.fileConfig(self.log_conf_file)
        return logging.getLogger("logError")


class LogFactory:

    def __init__(self):
        self.log_level = get_log_level("conf.yaml")
        self.log_set = {
            "NOTSET": LogDebug(),
            "DEBUG": LogDebug(),
            "INFO": LogDebug(),
            "WARN": LogWarn(),
            "ERROR": LogError(),
            "CRITICAL": LogError()
        }

    def logger(self):
        return self.log_set[self.log_level]


if __name__ == "__main__":
    log_factory = LogFactory()
    logger = log_factory.logger().get_logger()

    logger.debug("this is debug message")
    logger.info("this is info message")
    logger.warn("this is warn message")
    logger.error("this is error message")
    logger.critical("this is critical message")
