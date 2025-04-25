class ImPage():
    def __init__(self, name: str):
        self.name = name
        self.kv = {}

    def __getitem__(self, item):
        return self.kv[item]


class ImMemCache():
    def __init__(self):
        self.pages = {}

    def add(self, txt: str, value):
        self.pages[txt] = [
                {
                    "hit": 0
                },
                value,
            ]

    def remove(self, txt):
        self.pages.pop(txt)

    def set(self, txt, value):
        self.pages[txt][1] = value

    def get(self, txt):
        self.pages[txt][0]["hit"] += 1
        return self.pages[txt][1]

    def exists(self, txt):
        return txt in self.pages

    def __iter__(self):
        return self.pages

    def __item__(self, item):
        return self.pages[item]


class CacheFunc(object):
    def __init__(self, fn, args: tuple = ()):
        self.fn = fn
        self.args = args

    def __call__(self):
        return self.fn(*self.args)

    def __hash__(self):
        return hash(f"{self.fn.__self__.__class__.__name__}{self.args}")

def cache_txt(big: str, small: str = ""):
    return hash(f"{big}{small}")

class ImCache():
    memcache = ImMemCache()
