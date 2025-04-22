from unittest import TestCase
from .procmeminfo import FileUtilProcMemInfo

class TestFileUtilProcMemInfo(TestCase):
    def test_list(self):
        pmi = FileUtilProcMemInfo()
        pmi.list()
