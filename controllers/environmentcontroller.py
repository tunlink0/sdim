from controllers.controller import Controller
from fileutils.proccpuinfo import FileUtilProcCpuInfo
from fileutils.procmeminfo import FileUtilProcMemInfo
from fileutils.procuptime import FileUtilProcUptime
from fileutils.procversion import FileUtilProcVersion


class EnvironmentController(Controller):
    def __init__(self):
        super().__init__("environment")
        self.procmeminfo = FileUtilProcMemInfo()
        self.proccpuinfo = FileUtilProcCpuInfo()
        self.procversion = FileUtilProcVersion()
        self.procuptime = FileUtilProcUptime()

    def internal_run(self, path: str, query: str):
        if path == "/memory":
            return self.cache_call(self.procmeminfo.list)
        if path == "/cpu":
            return self.cache_call(self.proccpuinfo.list)
        if path == "/version":
            return self.cache_call(self.procversion.list)
        if path == "/uptime":
            return self.nocache_call(self.procuptime.list)
        elif path == "/all":
            return {
                "memory": self.cache_call(self.procmeminfo.list),
                "cpu": self.cache_call(self.proccpuinfo.list),
                "version": self.cache_call(self.procversion.list),
                "uptime": self.nocache_call(self.procuptime.list)
            }
        else:
            return None