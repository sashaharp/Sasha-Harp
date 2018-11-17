from math import sqrt

class Rectangle(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def Flaeche(self):
        return abs((self.p2[1]-self.p1[1])*(self.p2[0]-self.p1[0]))
    def Umfang(self):
        return ((self.p2[1]-self.p1[1]))*2+2*(self.p2[0]-self.p1[0])
    def Mitte(self):
        return ((self.p2[0]-self.p1[0])/2 + self.p1[0],(self.p2[1]-self.p1[1])/2 + self.p1[1])

class Triangle(object):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.__l1 = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        self.__l2 = sqrt((p2[0]-p3[0])**2+(p2[1]-p3[1])**2)
        self.__l3 = sqrt((p3[0]-p1[0])**2+(p3[1]-p1[1])**2)
    def Umfang(self):
        return self.__l1 + self.__l2 + self.__l3
    def Flaeche(self):
        s = (self.__l1+self.__l2+self.__l3)/2
        return sqrt(s*(s-self.__l1)*(s-self.__l2)*(s-self.__l3))
    def Schwerpunkt(self):
        return ((self.p1[0]+self.p2[0]+self.p3[0])/3,(self.p1[1]+self.p2[1]+self.p3[1])/3)