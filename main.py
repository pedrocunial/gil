from parser import parser, variables


# https://www.dabeaz.com/ply/ply.html
data = '''

# coment xd

y := 3
out y

x := (9 + 4 * 10 + -20  *2)
out x

'''

result = parser.parse(data)
result.eval(variables)
