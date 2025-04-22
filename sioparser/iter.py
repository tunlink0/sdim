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