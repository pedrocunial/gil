from lex import tokens
from symboltable import SymbolTable


class Node(object):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def eval(self, st):
        raise ValueError('Node class should not be directly evaluated')


class FuncDec(Node):
    def eval(self, st):
        st.set(self.value, self.children)


class FuncCall(Node):
    def eval(self, st):
        func_args, func_body = st.get(self.value)
        if len(func_args) != len(self.children):
            raise ValueError('Unmatching sizes between defined function args' +
                             f' and calling args ({len(func_args)} -- ' +
                             f'{len(self.children)})')
        inner_st = SymbolTable(father=st)
        inner_st.set(self.value, None)  # default return value
        for key, value in zip(func_args, self.children):
            inner_st.set(key, value.eval(st))
        func_body.eval(inner_st)
        return inner_st.get(self.value)


class CmdsOp(Node):
    def eval(self, st):
        for child in self.children:
            child.eval(st)


class TriOp(Node):
    def eval(self, st):
        if self.value == 'if':
            self.children[1].eval(st) if self.children[0].eval(st) \
                else self.children[2].eval(st)
        else:
            raise ValueError('Unexpected operator {} for triop'
                             .format(self.value))


class BinOp(Node):
    def eval_while(self, st):
        ''' extracted because the method was too long '''
        while self.children[0].eval(st):
            self.children[1].eval(st)

    def eval(self, st):
        if self.value == '+':
            return self.children[0].eval(st) + self.children[1].eval(st)
        elif self.value == '-':
            return self.children[0].eval(st) - self.children[1].eval(st)
        elif self.value == '/':
            return self.children[0].eval(st) // self.children[1].eval(st)
        elif self.value == '*':
            return self.children[0].eval(st) * self.children[1].eval(st)
        elif self.value == ':=':
            st.set(self.children[0], self.children[1].eval(st))
        elif self.value == '==':
            return self.children[0].eval(st) == self.children[1].eval(st)
        elif self.value == '<':
            return self.children[0].eval(st) < self.children[1].eval(st)
        elif self.value == '>':
            return self.children[0].eval(st) > self.children[1].eval(st)
        elif self.value == '&':
            return self.children[0].eval(st) and self.children[1].eval(st)
        elif self.value == '|':
            return self.children[0].eval(st) or self.children[1].eval(st)
        elif self.value == 'loop':
            self.eval_while(st)
        else:
            raise ValueError('Unexpected operator {} for binop'
                             .format(self.value))


class UnOp(Node):
    def eval(self, st):
        if self.value == '+':
            return +self.children[0].eval(st)
        elif self.value == '-':
            return -self.children[0].eval(st)
        elif self.value == 'out':
            print(self.children[0].eval(st))
        elif self.value == '!':
            return not self.children[0].eval(st)
        else:
            raise ValueError('Unexpected operator {} for unop'
                             .format(self.value))


class Input(Node):
    def eval(self, st):
        return int(input('input: '))


class IntVal(Node):
    def eval(self, st):
        return int(self.value)


class VarVal(Node):
    def eval(self, st):
        return st.get(self.value)


class NoOp(Node):
    def __init__(self, value=None, children=None):
        pass

    def eval(self, st):
        pass
