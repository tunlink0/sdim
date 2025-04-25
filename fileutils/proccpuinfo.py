import dictobject
from sioparser.listparser import ListParser, BlockParser
from .FileUtilWrapper import FileUtilWrapper

class FileUtilProcCpuInfo(FileUtilWrapper):
    def __init__(self):
        super().__init__("proccpuinfo")

    def list(self):
        parser = BlockParser(r"^(?P<label>\w+)\s+:\s+(?P<value>\w+)", "^$")
        return parser(self.read("/proc/cpuinfo")).to_dict()




