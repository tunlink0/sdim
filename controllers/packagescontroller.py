from binutils.aptget import BinUtilAptGet
from binutils.dpkg import BinUtilDpkg
from controllers.controller import Controller


class PackagesController(Controller):
    def __init__(self):
        super().__init__("packages")
        self.dpkg = BinUtilDpkg()
        self.aptget = BinUtilAptGet()

    def internal_run(self, path: str, query: str):
        if path == "/list":
            return self.cache_call(self.dpkg.list)
        elif path == "/update":
            return self.nocache_call(self.aptget.update)
        else:
            return None

    def list(self):
        return self.dpkg.list()
