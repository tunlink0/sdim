from abc import abstractmethod

import imcache.cache
from binutils import binutilwrapper
from binutils.dpkg import BinUtilDpkg
from fileutils.proccpuinfo import FileUtilProcCpuInfo
from fileutils.procmeminfo import FileUtilProcMemInfo
from fileutils.procversion import FileUtilProcVersion
from imcache.cache import cache_txt, CacheFunc


class Controller:


    def __init__(self, name: str):
        self.name = name
        self.memcache = imcache.cache.ImCache.memcache

    @abstractmethod
    def internal_run(self, path: str, query: str):
        pass

    def run(self, path: str, query: str):
        return self.internal_run(path, query)

    def cache_call(self, fn: CacheFunc):
        txt = hash(fn)
        if txt in self.memcache.pages:
            return self.memcache.pages[txt]
        else:
            out = fn()
            self.memcache.pages[txt] = out
            return out

class CliDpkgController(Controller):
    def __init__(self):
        super().__init__("dpkg")
        self.dpkg = BinUtilDpkg()

    def internal_run(self, path: str, query: str):
        if path == "/list":
            return self.cache_call(CacheFunc(self.dpkg.list))

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
            return self.cache_call(CacheFunc(self.procmeminfo.list))
        if path == "/cpu":
            return self.cache_call(CacheFunc(self.proccpuinfo.list))
        if path == "/version":
            return self.cache_call(CacheFunc(self.procversion.list))
        elif path == "/all":
            return {
                "memory": self.cache_call(CacheFunc(self.procmeminfo.list)),
                "cpu": self.cache_call(CacheFunc(self.proccpuinfo.list)),
                "version": self.cache_call(CacheFunc(self.procversion.list))
            }