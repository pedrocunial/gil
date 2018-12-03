class SymbolTable:
    def __init__(self, father=None, st={}):
        self.st = st
        self.father = father

    def get(self, key):
        if key not in self.st:
            if self.father is None:
                raise ValueError(f'Unknown key {key}')
            else:
                return self.father.get(key)
        return self.st[key]

    def contains_above(self, key):
        father = self.father
        while father is not None and key not in father:
            father = father.father
        return father

    def set(self, key, value):
        if key not in self.st:
            father = self.contains_above(key)
            if father is not None:
                father.set(key, value)
                return
        self.st[key] = value
