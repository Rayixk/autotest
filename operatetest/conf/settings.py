# coding: utf-8
# created by yang

import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




LOG = {
    "file_name": "test.log",
    "console_level": "DEBUG",
    "file_level": "DEBUG",
    "pattern": "'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
}
