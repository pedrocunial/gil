from parser import parser, variables

if __name__ == '__main__':

    # https://www.dabeaz.com/ply/ply.html
    with open('../examples/simple.gil', 'r') as f:
        data = f.read()

    result = parser.parse(data)
    result.eval(variables)
