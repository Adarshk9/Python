class Line:
    def __init__(self,l):
        self.length = l
    def showlength(self):
        print("Length = ",self.length)
    def __add__(self,other):
        return Line(self.length+other.length)
l1 = Line(10)
l2 = Line(20)
l3 = l1+l2
l3.showlength()
