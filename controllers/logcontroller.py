from controllers.controller import Controller
from fileutils.varlogsdim import FileUtilVarLogSdim


class LogsController(Controller):
    def __init__(self):
        super().__init__("environment")
        self.varlogsdim = FileUtilVarLogSdim()

    def internal_run(self, path: str, query: str):
        if path.startswith("/view/"):
            reference = path.split("/")[-1]
            return self.nocache_call(self.varlogsdim.load, (reference,))