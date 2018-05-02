import unittest
from ..utils.log import Logger
from aw import Driver


class TestCase(unittest.TestCase):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.log = Logger(self.__class__.__name__).get_logger()
        self.driver = Driver.driver()



