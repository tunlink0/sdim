import dictobject
from sioparser.listparser import ListParser, BlockParser
from .FileUtilWrapper import FileUtilWrapper

class FileUtilProcCpuInfo(FileUtilWrapper):
    def __init__(self):
        super().__init__("proccpuinfo")

    def list(self):
        parser = BlockParser(r"^(?P<label>[\w\s]+)\s+:\s+(?P<value>[\S\s]+)", "^$")
        out = []
        for item in parser(self.read("/proc/cpuinfo")).to_dict():
            out.append({
                "cpu_num": int(item["processor"]),
                "cpu_id": int(item["physical_id"]),
                "cpu_core_id": int(item["core_id"]),
                "cpu_family": int(item["cpu_family"]),
                "cpu_model": int(item["model"]),
                "cpu_clock": float(item["cpu_MHz"]),
                "cpu_cache_size": int(item["cache_size"].split(" ")[0]),
                "vendor_name": item["vendor_id"],
                "model_name": item["model_name"],
            })
        return out




