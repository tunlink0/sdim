from sioparser.listparser import ListParser
from .FileUtilWrapper import FileUtilWrapper

class ProcMemInfoProfile():
    def __init__(self, l):
        self.mem_total = int(l["MemTotal"])
        self.mem_free = int(l["MemFree"])
        self.mem_available = int(l["MemAvailable"])
        self.swap_total = int(l["SwapTotal"])
        self.swap_free = int(l["SwapFree"])

class FileUtilProcMemInfo(FileUtilWrapper):
    def __init__(self):
        super().__init__("procmeminfo")

    def list(self):
        parser = ListParser(r"^(?P<label>\w+):\s+(?P<value>\d+)\s+kB")
        return ProcMemInfoProfile(parser(self.read("/proc/meminfo")).to_dict())



