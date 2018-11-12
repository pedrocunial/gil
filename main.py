from lex import lexer


# https://www.dabeaz.com/ply/ply.html
data = '''
3 + 4 * 10 +
        -20
           *2
'''

lexer.input(data)

# tokenize
while True:
    token = lexer.token()
    if not token:
        break  # no more input
    print(token)
