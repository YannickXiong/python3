# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 20:16
# @Author  : Yannick
# @File    : log.py


import yaml
import logging
import logging.config


def get_log_level(config_file):

    try:
        with open(config_file) as fp:
            config = yaml.load(fp)

        if config.__contains__("loglevel"):
            return config["loglevel"].upper()
        else:
            raise KeyError("loglevel doesn't exist in config file!")
    except Exception as e:
        print(e)
    finally:
        return "DEBUG"


class Log:

    def __init__(self):
        self.log_level = get_log_level("conf.yaml")
        self.log_conf_file = "log_demo.conf"



class LogDebug(Log):

    def get_logger(self):
        logging.config.fileConfig(self.log_conf_file)
        print("LogDebug")
        return logging.getLogger("logDebug")


class LogInfo(Log):

    def get_logger(self):
        logging.config.fileConfig(self.log_conf_file)
        print("LogInfo")
        return logging.getLogger("logInfo")


class LogError(Log):

    def get_logger(self):
        logging.config.fileConfig(self.log_conf_file)
        print("LogError")
        return logging.getLogger("logError")


class LogFactory:

    def __init__(self):
        self.log_level = get_log_level("conf.yaml")
        self.log_set = {
            "DEBUG": LogDebug(),
            "INFO": LogInfo(),
            "ERROR": LogError()
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
