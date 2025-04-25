import dictobject
from sioparser.listparser import ListParser
from .FileUtilWrapper import FileUtilWrapper

class FileUtilProcMemInfo(FileUtilWrapper):
    def __init__(self):
        super().__init__("procmeminfo")

    def list(self):
        parser = ListParser(r"^(?P<label>\w+):\s+(?P<value>\d+)\s+kB")
        lpmi = parser(self.read("/proc/meminfo")).to_dict()
        return {
            "mem_total": int(lpmi["MemTotal"]),
            "mem_free": int(lpmi["MemFree"]),
            "mem_available": int(lpmi["MemAvailable"]),
            "swap_total": int(lpmi["SwapTotal"]),
            "swap_free": int(lpmi["SwapFree"]),
        }




