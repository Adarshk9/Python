def natural():
    n = 1
    while(n<=100):
        yield n
        n+=1
g = natural()
for i in g:
    print(i)
print(next(g))

'''
def f1():
    yield 10
    yield 20
    yield 30
g = f1()
for e in g:
    print(e)
print(g)
'''