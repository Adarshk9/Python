class A:
    def function(self):
        self.a = 5
        print(self.a)
obj = A()
obj.function()
A.function(obj)

class B:
    @staticmethod
    def function2(self):
        self.b = 55
        print(self.b)
obj2 = B()
obj2.function2(obj2)

class C:
    @classmethod
    def function3(cls):
        cls.x = 20
        print(cls.x)
C.function3()
obj3 = C()
obj3.function3()
