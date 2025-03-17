def a():
    print('start of a()')
    b()

def b():
    print('start of b()')
    c()

def c():
    print('start of c()')
    42 / 0

a()