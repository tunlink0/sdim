from abc import abstractmethod
from binutils import binutilwrapper


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
        self.dpkg = cliwrapper.BinUtilDpkg()

    def internal_run(self, path: str, query: str):
        if path == "/list":
            return self.list()

    def list(self):
        return self.dpkg.list()
