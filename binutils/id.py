import dictobject
import subprocess
from .binutilwrapper import BinUtilWrapper
from sioparser.listparser import ListParser


class BinUtilIdUser(dictobject.DictObject):
    def __init__(self, userid: str, username: str, groupid: str, groupname: str):
        self.userid = int(userid)
        self.username = username
        self.groupid = int(groupid)
        self.groupname = groupname

    def to_dict(self):
        return {
            "userid": self.userid,
            "username": self.username,
            "groupid": self.groupid,
            "groupname": self.groupname,
        }
class BinUtilId(BinUtilWrapper):
    def __init__(self):
        super().__init__("id")

    def id(self):
        out = subprocess.run(["id"], capture_output=True)
        strout = "".join([chr(int(b)) for b in out.stdout])
        clp = ListParser(
            r"^uid=(?P<uidnum>\d+)\((?P<uidnam>\S+)\) "
            r"gid=(?P<gidnum>\d+)\((?P<gidnam>\S+)\)")

        l = clp(strout.split("\n"))
        return BinUtilIdUser(*l.tuple[0][0])