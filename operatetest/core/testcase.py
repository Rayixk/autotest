import unittest
from ..utils.log import logger


class TestCase(unittest.TestCase):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.log = logger



