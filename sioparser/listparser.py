import re
from .iter import CliIter

class ItemList(object):
    def __init__(self, items):
        self.tuple = items

    def to_dict(self):
        d = {}
        for t in self.tuple:
            k, v = t[0]
            d[k] = v
        return d

class ListParser(object):
    def __init__(self, regex_line: str):
        self.regex_line = re.compile(regex_line)

    def __call__(self, items):
        it = CliIter(items)
        out = []
        while not it.end():
            o = self.regex_line.findall(it.line())
            if o:
                out.append(o)
            # else:
            #     print(it.line())
            it.next()
        return ItemList(out)


