class SymbolTable:
    def __init__(self, st={}):
        self.st = st

    def get(self, key):
        if key not in self.st:
            raise ValueError(f'Unknown key {key}')
        return self.st[key]

    def set(self, key, value):
        self.st[key] = value
