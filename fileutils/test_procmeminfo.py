from unittest import TestCase
from .procmeminfo import FileUtilProcMemInfo

class TestFileUtilProcMemInfo(TestCase):
    def test_list(self):
        pmi = FileUtilProcMemInfo()
        ppmi = pmi.list()
        self.assertTrue(ppmi.mem_free > 0)
        self.assertTrue(ppmi.mem_total > 0)

