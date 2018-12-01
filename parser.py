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


def p_stmt(p):
    '''stmt : assign
            | out'''
    p[0] = p[1]


def p_assign(p):
    'assign : ID ASSIGNER expression'
    p[0] = nd.BinOp(':=', [p[1], p[3]])


def p_out(p):
    'out : PRINT expression'
    p[0] = nd.UnOp(p[1], [p[2]])


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = nd.BinOp('+', [p[1], p[3]])


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = nd.BinOp('-', [p[1], p[3]])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term MULT factor'
    p[0] = nd.BinOp('*', [p[1], p[3]])


def p_term_div(p):
    'term : term DIV factor'
    p[0] = nd.BinOp('/', [p[1], p[3]])


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
              | MINUS expression %prec UMINUS'''
    p[0] = nd.UnOp(p[1], [p[2]])


def p_factor_expr(p):
    'factor : OPEN_PARENT expression CLOSE_PARENT'
    p[0] = p[2]


def p_empty(p):
    'empty : '


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
        print(result.eval(variables))
