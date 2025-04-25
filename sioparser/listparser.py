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


class BlockList(object):
    def __init__(self):
        self.blocks: list[ItemList] = []

    def append(self, item: ItemList):
        self.blocks.append(item)

    def to_dict(self):
        d = []
        for i in self.blocks:
            d.append(i.to_dict())
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


class BlockParser(object):
    def __init__(self, regex_line: str, regex_delim: str):
        self.regex_line = re.compile(regex_line)
        self.regex_delim = re.compile(regex_delim)

    def __call__(self, items):
        it = CliIter(items)
        out = []
        blocks = BlockList()
        while not it.end():
            if self.regex_delim.match(it.line()):
                blocks.append(ItemList(out))
                out = []
            else:
                o = self.regex_line.findall(it.line())
                if o:
                    out.append(o)
            it.next()
        if len(out) > 0:
            blocks.append(ItemList(out))
        return blocks
