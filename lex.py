import ply.lex as lex


reserved = {
    'i': 'IF',
    'e': 'ELSE',
    'l': 'LOOP',
    'out': 'PRINT',
    'in': 'INPUT'
}

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'OPEN_PARENT',
    'CLOSE_PARENT',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'ID',
    'COMMENT',
    'ASSIGNER',
    'EQ',
    'LT',
    'GT',
    'AND',
    'OR',
    'NOT',
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_OPEN_PARENT = r'\('
t_CLOSE_PARENT = r'\)'
t_OPEN_BRACKET = r'\{'
t_CLOSE_BRACKET = r'\}'
t_ASSIGNER = r'\:='
t_EQ = r'\=='
t_LT = r'\<'
t_GT = r'\>'
t_AND = r'\&'
t_OR = r'\|'
t_NOT = r'\!'

t_ignore = ' \t'  # ignorar espacos e tabs


# a regex "no meio do nada" faz parte da sintaxe do ply
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # palavras reservadas
    return t


def t_COMMENT(t):
    r'\#.*'
    pass  # nao retornar implica em ignorar o token


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# newline precisa ser definido para contar as linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # mais de um \n pode ser pego na regex


def t_error(t):
    print(f'Illegal character {t.value[0]}')
    t.lexer.skip(1)


lexer = lex.lex(optimize=1)
