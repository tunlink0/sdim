import subprocess
from sioparser.listparser import ListParser
import dictobject
from binutils.binutilwrapper import BinUtilWrapper

class BinUtilDpkgItem(dictobject.DictObject):
    def __init__(self, states: str, name: str, version: str, arch: str, description: str):
        self.name = name
        self.version = version
        self.arch = arch
        self.description = description
        self.state_desired = states[0]
        self.state_current = states[1]
        self.state_error = states[2]

    def to_dict(self):
        return {
            "name": self.name,
            "version": self.version,
            "arch": self.arch,
            "description": self.description,
            "state_desired": self.state_desired,
            "state_current": self.state_current,
            "state_error": self.state_error,
        }


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
            packages.append(BinUtilDpkgItem(*i[0]))
        return packages