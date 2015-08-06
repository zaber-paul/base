import json


class MultiKeyDict(object):

    def __init__(self, m):
        self.element = {
            "keys" : m,
            "value" : {}
            }

    def dump(self):
        print(json.dumps(self.element, indent=4))

    def set(self, d):
        for key in d:
           self.__setitem__(key, d[key])

    def _getkey(self, key):
        for k in self.element["keys"]:
            if key in k:
                return k[0]
        raise Exception("key not found: " + key)

    def __getitem__(self, key):
        return self.element["value"][self._getkey(key)]

    def __setitem__(self, key, value):
        self.element["value"][self._getkey(key)] = value

    def __str__(self):
        return str(dict(self.element["value"]))
