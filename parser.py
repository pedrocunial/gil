import ply.yacc as yacc
import node as nd

from lex import tokens
from symboltable import SymbolTable


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UPLUS', 'UMINUS'),
)

variables = SymbolTable()


def p_stmts(p):
    '''stmts : stmt stmts
             | empty'''
    if len(p) == 3:
        p[0] = nd.CmdsOp(None, [p[1], p[2]])
    else:
        p[0] = p[1]


def p_stmt(p):
    '''stmt : assign
            | out
            | if
            | loop'''
    p[0] = p[1]


def p_if(p):
    '''if : IF relexp OPEN_BRACKET stmts CLOSE_BRACKET ELSE OPEN_BRACKET stmts CLOSE_BRACKET
          | IF relexp OPEN_BRACKET stmts CLOSE_BRACKET'''
    if len(p) == 10:
        p[0] = nd.TriOp('if', [p[2], p[4], p[8]])
    else:
        p[0] = nd.TriOp('if', [p[2], p[4], nd.NoOp()])


def p_if_error(p):
    '''if : IF error OPEN_BRACKET stmts CLOSE_BRACKET ELSE OPEN_BRACKET stmts CLOSE_BRACKET
          | IF error OPEN_BRACKET stmts CLOSE_BRACKET'''
    print(f'Syntax error in if expression {p}')


def p_loop(p):
    'loop : LOOP relexp OPEN_BRACKET stmts CLOSE_BRACKET'
    p[0] = nd.BinOp('loop', [p[2], p[4]])


def p_loop_error(p):
    'loop : LOOP error OPEN_BRACKET stmts CLOSE_BRACKET'
    print(f'Syntax error in loop expression {p}')


def p_assign(p):
    'assign : ID ASSIGNER relexp'
    p[0] = nd.BinOp(':=', [p[1], p[3]])


def p_out(p):
    'out : PRINT relexp'
    p[0] = nd.UnOp(p[1], [p[2]])


def p_relexp(p):
    '''relexp : expression
              | relexp GT relexp
              | relexp EQ relexp
              | relexp LT relexp'''
    if len(p) == 2:  # relexp : expression
        p[0] = p[1]
    else:
        p[0] = nd.BinOp(p[2], [p[1], p[3]])


def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = nd.BinOp('+', [p[1], p[3]])


def p_expression_or(p):
    'expression : expression OR relexp'
    p[0] = nd.BinOp('|', [p[1], p[3]])


def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = nd.BinOp('-', [p[1], p[3]])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term MULT expression'
    p[0] = nd.BinOp('*', [p[1], p[3]])


def p_term_div(p):
    'term : term DIV expression'
    p[0] = nd.BinOp('/', [p[1], p[3]])


def p_term_and(p):
    'term : term AND relexp'
    p[0] = nd.BinOp('&', [p[1], p[3]])


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = nd.IntVal(p[1], None)


def p_factor_id(p):
    'factor : ID'
    p[0] = nd.VarVal(p[1], None)


def p_factor_input(p):
    'factor : INPUT'
    p[0] = nd.Input(None, None)


def p_factor_sign_num(p):
    '''factor : PLUS expression %prec UPLUS
              | MINUS expression %prec UMINUS
              | NOT relexp'''
    p[0] = nd.UnOp(p[1], [p[2]])


def p_factor_expr(p):
    'factor : OPEN_PARENT relexp CLOSE_PARENT'
    p[0] = p[2]


def p_empty(p):
    'empty : '
    p[0] = nd.NoOp()


# Error rule for syntax errors
def p_error(p):
    print(f'Syntax error at {repr(p)}')


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
        print(result.eval(variables))
