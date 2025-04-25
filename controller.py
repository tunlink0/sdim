from abc import abstractmethod
from binutils import binutilwrapper
from binutils.dpkg import BinUtilDpkg
from fileutils.proccpuinfo import FileUtilProcCpuInfo
from fileutils.procmeminfo import FileUtilProcMemInfo
from fileutils.procversion import FileUtilProcVersion


class Controller:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def internal_run(self, path: str, query: str):
        pass

    def run(self, path: str, query: str):
        return self.internal_run(path, query)

class CliDpkgController(Controller):
    def __init__(self):
        super().__init__("dpkg")
        self.dpkg = BinUtilDpkg()

    def internal_run(self, path: str, query: str):
        if path == "/list":
            return self.list()

    def list(self):
        return self.dpkg.list()

class HostEnvController(Controller):
    def __init__(self):
        super().__init__("hostenv")
        self.procmeminfo = FileUtilProcMemInfo()
        self.proccpuinfo = FileUtilProcCpuInfo()
        self.procversion = FileUtilProcVersion()

    def internal_run(self, path: str, query: str):
        if path == "/memory":
            return self.procmeminfo.list()
        if path == "/cpu":
            return self.proccpuinfo.list()
        if path == "/version":
            return self.procversion.list()
        elif path == "/all":
            return {
                "memory": self.procmeminfo.list(),
                "cpu": self.proccpuinfo.list(),
                "version": self.procversion.list()
            }