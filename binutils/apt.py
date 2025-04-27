import subprocess
from binutils.binutilwrapper import BinUtilWrapper, subprocess_console_response
from sioparser.listparser import ListParser, build_list_from_console_out


class BinUtilApt(BinUtilWrapper):
    def __init__(self):
        super().__init__("aptget")

    def update(self):
        out = subprocess.run(["apt-get", "update"], capture_output=True)

        return subprocess_console_response(out.returncode, out.stdout, out.stderr)

    def list_upgrade(self):
        out = subprocess.run(["apt", "list", "--upgradable"], capture_output=True)
        l = build_list_from_console_out(out.stdout,
                                            r"(?P<name>[\S\s]+)/"
                                            r"(?P<repo>[\S]+)\s"
                                            r"(?P<version>[\S]+)\s"
                                            r"(?P<arch>[\S]+)\s"
                                            r"\[upgradable\sfrom:\s"
                                            r"(?P<old>[\S]+)"
                                            r"\]")
        upgrades = []
        for i in l.tuple:
            upgrades.append({
                "package": i[0][0],
                "new_version": i[0][2],
                "cur_version": i[0][4],
            })

        return upgrades

