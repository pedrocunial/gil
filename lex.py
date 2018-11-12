import ply.lex as lex


tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'OPEN_PARENT',
    'CLOSE_PARENT',
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_OPEN_PARENT = r'\('
t_CLOSE_PARENT = r'\)'

t_ignore = ' \t'  # ignorar espacos e tabs


# a regex "no meio do nada" faz parte da sintaxe do ply
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


lexer = lex.lex()
