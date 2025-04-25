import subprocess
from sioparser.listparser import ListParser
import dictobject
from binutils.binutilwrapper import BinUtilWrapper

class BinUtilDpkg(BinUtilWrapper):
    def __init__(self):
        super().__init__("dpkg")

    def list(self):
        out = subprocess.run(["dpkg", "--list"], capture_output=True)
        strout = "".join([chr(int(b)) for b in out.stdout])
        clp = ListParser(
            r"^(?P<states>\w\w[\w ])\s+"
            r"(?P<name>\S+)\s+"
            r"(?P<version>\S+)\s+"
            r"(?P<arch>\w+)\s+"
            r"(?P<desc>[\s\S]+)")

        l = clp(strout.split("\n"))
        packages = []
        for i in l.tuple:
            packages.append({
                "state_desired": i[0][0][0],
                "state_current": i[0][0][1],
                "state_error": i[0][0][2],
                "name": i[0][1],
                "version": i[0][2],
                "arch": i[0][3],
                "description": i[0][4],
            })
        return packages