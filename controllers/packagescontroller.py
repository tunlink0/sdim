from binutils.dpkg import BinUtilDpkg
from controllers.controller import Controller


class PackagesController(Controller):
    def __init__(self):
        super().__init__("packages")
        self.dpkg = BinUtilDpkg()

    def internal_run(self, path: str, query: str):
        if path == "/list":
            return self.cache_call(self.dpkg.list)
        else:
            return None

    def list(self):
        return self.dpkg.list()
