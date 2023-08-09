# обычная функция
def calk1(a, b):
    return a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk2, 5, 25)

# lambda функция

calk3 = lambda a,b: a + b

math(calk3, 5, 25)

math(lambda a,b: a + b, 5, 25)

