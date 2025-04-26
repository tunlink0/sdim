from sioparser.listparser import ListParser, BlockParser
from .FileUtilWrapper import FileUtilWrapper

class FileUtilProcUptime(FileUtilWrapper):
    def __init__(self):
        super().__init__("procuptime")

    def list(self):
        total, idle = self.read_line("/proc/uptime").split(" ",1)
        return {
            "total": float(total)
        }
