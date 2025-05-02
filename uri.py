import re


class Uri:
    def __init__(self, s: str):
        ss = s.split("?", 1)
        c = re.findall(r"(?P<scheme>\w+)://"
            r"(?P<authority>\w+)"
            r"(?P<path>[\w/]+)", ss[0])

        self.scheme, self.authority, self.path = c[0]
        paths = self.path.lstrip("/").split("/")
        self.module = paths[0]
        self.modpath = "/"+"/".join(paths[1:])

        try:
            self.query_string = ss[1]
            self.query_list = self.query_string.split("&")
        except IndexError as e:
            self.query_string = ""
            self.query_list = []


