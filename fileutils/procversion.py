import dictobject
from sioparser.listparser import ListParser
from .FileUtilWrapper import FileUtilWrapper

class FileUtilProcVersion(FileUtilWrapper):
    def __init__(self):
        super().__init__("procversion")

    def list(self):
        sv = self.read_line("/proc/version")
        return {
            "version": sv,
        }




