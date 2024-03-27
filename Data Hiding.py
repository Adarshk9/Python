class Test:
    x = 5
    __h = 10
    def __init__(self):
        self.__a = 100
print(Test._Test__h)
obj = Test()
print(obj.__dict__)