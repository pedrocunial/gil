import ply.yacc as yacc
from lex import tokens


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UPLUS', 'UMINUS'),
)

variables = {}


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term MULT factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIV factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_id(p):
    'factor : ID'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f'Undefined variable {p[1]}')
        p[0] = 0


def p_factor_sign_num(p):
    '''factor : PLUS expression %prec UPLUS
              | MINUS expression %prec UMINUS'''
    if p[1] == '+':
        p[0] = p[2]
    else:
        p[0] = -p[2]


def p_factor_expr(p):
    'factor : OPEN_PARENT expression CLOSE_PARENT'
    p[0] = p[2]


def p_assign(p):
    'assign : ID ASSIGNER expression'
    print('assign')
    variables[p[1]] = p[3]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':
    # debugging
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)
