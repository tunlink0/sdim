from sioparser.listparser import ListParser
from .FileUtilWrapper import FileUtilWrapper

class ProcMemInfoProfile():
    def __init__(self):
        pass

class FileUtilProcMemInfo(FileUtilWrapper):
    def __init__(self):
        super().__init__("procmeminfo")

    def list(self):
        parser = ListParser(r"^(?P<label>\w+):\s+(?P<value>\d+)\s+kB")
        out = parser(self.read("/proc/meminfo")).to_dict()
        print(out)


