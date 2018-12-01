from parser import parser, variables


# https://www.dabeaz.com/ply/ply.html
data = '''

# coment xd

y := 3
out y

x := (9 + 4 * 10 + -20  *2)
out x

l x > y {
y := y + 1
out y
}

i ((y - x) == 0) {
out 42
} e {
out 24
}

f double(value) {
double := value * 2
}

value := 2
out double(value)
out value

'''

result = parser.parse(data)
result.eval(variables)
