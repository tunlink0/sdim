import re


class CliIter(object):
    def __init__(self, lines: list[str], window_begin: int = 0):
        self.content = lines
        self.window_line = window_begin
        self.window_begin = window_begin
        self.window_end = len(lines)

    def line(self):
        if self.window_line == self.window_end:
            raise IndexError
        return self.content[self.window_line]

    def next(self):
        if self.window_line == self.window_end:
            raise IndexError
        self.window_line = self.window_line + 1

    def end(self):
        if self.window_line == self.window_end:
            return True
        return False


class CliListParser(object):
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
        return out

