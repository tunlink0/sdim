import subprocess
from binutils.binutilwrapper import BinUtilWrapper, subprocess_console_response

from sioparser.listparser import build_list_from_console_out
from sioparser.logreader import LogReader


class AptLogReader(LogReader):
    def __init__(self):
        super().__init__()

    def read_upgradable_list(self, t: tuple):
        if "upgrades" not in self.out:
            self.out["upgrades"] = []

        self.out["upgrades"].append({
            "package": t[0][0],
            "new_version": t[0][2],
            "cur_version": t[0][4],
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
        out = self.iv.run(["apt-get", "upgrade", "-qy"], log=True)
        regex = r"Get:\d (?P<uri>\S+) (?P<repo>\S+) (?P<rarch>\S+) (?P<name>\S+) (?P<arch>\S+) (?P<version>\S+) \[(?P<size>\d+)"
