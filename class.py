a = fourcal()
a.setdata(4,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
-
class FourCal:
    pass

a=FourCal()
print(type(a))
-
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
a=FourCal()
b=FourCal()
a.setdata(4,2)
FourCal.setdata(a, 4, 2)
b.setdata(3,7)
print(a.first)
print(b.first)
print(id(a.first))
print(id(b.first))
-
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
a = FourCal()
a.setdata(4,2)
a = a.add()
print(a)
-
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
a.setdata(4,2)
a = a.add()
print(a)
-
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal(4,2)
a.setdata(4,2)
a = a.add()
print(a)
-
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a=MoreFourCal(4,2)
a.pow()
-
class SafeFourCal(Fourcal):
    def div(self):
        if self.second == 0:    #나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second