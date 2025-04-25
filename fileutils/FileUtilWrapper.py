class FileUtilWrapper(object):
    def __init__(self, name: str):
        self.name = name

    def read(self, file: str) -> list[str]:
        with open(file) as fp:
            out = fp.read().splitlines()
            return out

    def read_line(self, file: str) -> str:
        with open(file) as fp:
            out = fp.read().splitlines()
            return out[0]