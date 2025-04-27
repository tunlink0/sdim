from binutils.apt import BinUtilApt
from binutils.dpkg import BinUtilDpkg
from controllers.controller import Controller


class PackagesController(Controller):
    def __init__(self):
        super().__init__("packages")
        self.dpkg = BinUtilDpkg()
        self.aptget = BinUtilApt()

    def internal_run(self, path: str, query: str):
        if path == "/list":
            return self.cache_call(self.dpkg.list)
        elif path == "/update":
            return self.nocache_call(self.aptget.update)
        elif path == "/upgradable":
            return self.nocache_call(self.aptget.list_upgrade)
        else:
            return None

    def list(self):
        return self.dpkg.list()
