# coding: utf-8
# created by yang

import os,sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
sys.path.insert(0,BASE_DIR)

DRIVER_PATH = os.path.join(BASE_DIR, 'drivers')
DATA_PATH = os.path.join(BASE_DIR, 'data')
LOG_PATH = os.path.join(BASE_DIR, 'log')
REPORT_PATH = os.path.join(BASE_DIR, 'report')

for path in [DRIVER_PATH,DATA_PATH,LOG_PATH,REPORT_PATH]:
    if not os.path.exists(path):
        os.makedirs(path)


URL='http://www.baidu.com'
LOG = {
    "file_name": "test.log",
    "backup": 5,
    "console_level": "WARNING",
    "file_level": "DEBUG",
    "pattern": '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
}

