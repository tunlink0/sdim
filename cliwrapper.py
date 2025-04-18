import subprocess
import cliparser
import dictobject


class CliWrapper:
    def __init__(self, cli_name):
        self.cli_name = cli_name


class CliDpkgPackageItem(dictobject.DictObject):
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


class CliWrapperDpkg(CliWrapper):
    def __init__(self):
        super().__init__("dpkg")

    def list(self):
        out = subprocess.run(["dpkg", "--list"], capture_output=True)
        strout = "".join([chr(int(b)) for b in out.stdout])
        clp = cliparser.CliListParser(
            r"^(?P<states>\w\w[\w ])\s+"
            r"(?P<name>\S+)\s+"
            r"(?P<version>\S+)\s+"
            r"(?P<arch>\w+)\s+"
            r"(?P<desc>[\s\S]+)")

        l = clp(strout.split("\n"))
        packages = []
        for i in l:
            packages.append(CliDpkgPackageItem(*i[0]))
        return packages