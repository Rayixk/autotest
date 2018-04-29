# coding: utf-8
# created by yang
import logging
from logging import FileHandler

class Logger(object):
    def __init__(self, log_file_name,logger_name='operatetest'):
        self.log_file_name = log_file_name
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)

        # level
        self.console_output_level = "DEBUG"
        self.file_output_level = "DEBUG"

        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        我们这里添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
        两个句柄的日志级别不同，在配置文件中可设置。
        """
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        console_handler.setLevel(self.console_output_level)
        self.logger.addHandler(console_handler)

        file_handler = FileHandler(filename=self.log_file_name,encoding='utf-8')
        file_handler.setFormatter(self.formatter)
        file_handler.setLevel(self.file_output_level)
        self.logger.addHandler(file_handler)

        return self.logger

logger_a = Logger("loga.txt").get_logger()
logger_b = Logger("logb.txt").get_logger()

print(id(logger_a))
print(id(logger_b))

logger_a.info("xxx")
logger_a.info("bbb")