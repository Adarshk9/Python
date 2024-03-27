a = 10
class Something:
    x = 100 #This is class object variable
    def f1(self):
        self.a = 10
    def __init__(self):
        self.b = 20
        print(self.b)
Ob = Something()
Ob.f1()
print(Ob.x)
print(Ob.a)
