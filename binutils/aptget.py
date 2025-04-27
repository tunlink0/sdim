import subprocess
from binutils.binutilwrapper import BinUtilWrapper, subprocess_console_response


class BinUtilAptGet(BinUtilWrapper):
    def __init__(self):
        super().__init__("aptget")

    def update(self):
        out = subprocess.run(["apt-get", "update"], capture_output=True)

        return subprocess_console_response(out.returncode, out.stdout, out.stderr)

    def list_upgrade(self):
        pass