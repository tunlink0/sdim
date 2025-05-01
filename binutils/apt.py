import subprocess
from binutils.binutilwrapper import BinUtilWrapper, subprocess_console_response
from sioparser.logreader import LogReader


class AptLogReader(LogReader):
    def __init__(self):
        super().__init__()

    def read_upgradable_list(self, tup: tuple):
        if "upgrades" not in self.out:
            self.out["upgrades"] = []

        self.out["upgrades"].append({
            "package": tup[0][0],
            "new_version": tup[0][2],
            "cur_version": tup[0][4],
        })

    def upgrade_downloads(self, tup: tuple):
        if "download" not in self.out:
            self.out["download"] = []

        self.out["download"].append({
            "package": tup[0][3],
            "version": tup[0][5],
            "size": tup[0][6]
        })

    def upgrade_unpack(self, tup: tuple):
        if "unpack" not in self.out:
            self.out["unpack"] = []

        self.out["unpack"].append({
            "package": tup[0][0],
            "old_version": tup[0][2],
            "new_version": tup[0][1],
        })

    def upgrade_setup(self, tup, tuple):
        if "setup" not in self.out:
            self.out["setup"] = []
        self.out["setup"].append({
            "package": tup[0][0],
            "version": tup[0][1],
        })


class BinUtilApt(BinUtilWrapper):
    def __init__(self):
        super().__init__("aptget")

    def update(self):
        out = subprocess.run(["apt-get", "update", "-q"], capture_output=True)
        return subprocess_console_response(out.returncode, out.stdout, out.stderr)

    def list_upgrade(self):
        lr = AptLogReader()
        self.iv.callback(lr.read_upgradable_list,
                         r"(?P<name>[\S\s]+)/"
                         r"(?P<repo>[\S]+)\s"
                         r"(?P<version>[\S]+)\s"
                         r"(?P<arch>[\S]+)\s"
                         r"\[upgradable\sfrom:\s"
                         r"(?P<old>[\S]+)"
                         r"\]")

        out = self.iv.run(["apt", "list", "--upgradable"], True)
        return {"reference": out.reference, "upgrades": lr.to_dict()["upgrades"]}

    def upgrade_all(self):
        lr = AptLogReader()
        self.iv.callback(lr.upgrade_downloads,
                         r"Get:\d (?P<uri>\S+) (?P<repo>\S+) (?P<rarch>\S+) (?P<name>\S+) (?P<arch>\S+) (?P<version>\S+) \[(?P<size>\d+)")

        self.iv.callback(lr.upgrade_unpack,
                         r"Unpacking (?P<name>\S+) \((?P<new>\S+)\) over \((?P<old>\S+)\)")

        self.iv.callback(lr.upgrade_setup,
                         r"Setting up (?P<name>\S+) \((?P<new>\S+)\)")

        out = self.iv.run(["apt-get", "upgrade", "-qy"], log=True)
        return {"reference": out.reference, "upgraded": lr.to_dict()}