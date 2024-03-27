x =20
def f1():
    x = 10
    print(id(x))
    print(x)
    d = globals()
    d['x'] = 30
f1()
print(x)
print(id(x))