from abc import abstractmethod


class DictObject(object):
    @abstractmethod
    def to_dict(self):
        pass
