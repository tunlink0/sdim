from abc import abstractmethod

import imcache.cache
from imcache.cache import CacheFunc


class Controller:

    def __init__(self, name: str):
        self.name = name
        self.memcache = imcache.cache.ImCache.memcache

    @abstractmethod
    def internal_run(self, path: str, query: str):
        pass

    def run(self, path: str, query: str):
        return self.internal_run(path, query)

    def cache_call(self, fn, args: tuple = ()):
        cfn = CacheFunc(fn, args)
        txt = hash(cfn)
        if self.memcache.cached(txt):
            return self.memcache.get(txt)
        else:
            out = cfn()
            self.memcache.add(txt, out)
            return out

    def nocache_call(self, fn, args: tuple = ()):
        return fn(*args)

