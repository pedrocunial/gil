from lex import lexer


# https://www.dabeaz.com/ply/ply.html
data = '''

x := (3 + 4 * 10 +
        -20
           *2)
i x < 3 {
    y := 2
} e {
    y := x
}

i x == y {
    z := 1
} e {
    z := 0
}
'''

lexer.input(data)

# tokenize
while True:
    token = lexer.token()
    if not token:
        break  # no more input
    print(f'type: {token.type}\nvalue: {token.value}\n' +
          f'line number: {token.lineno}\n' +
          f'absolute pos: {token.lexpos}\n================')
