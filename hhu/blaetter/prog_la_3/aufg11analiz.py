from math import sqrt
class rect():
    def __init__(self,p0,p1):
        self.p0 = p0
        self.p1 = p1

    def A(self):
        return (self.p1[1]-self.p0[1])*(self.p1[0]-self.p0[0])

    def U(self):
        return (self.p1[1]-self.p0[1])*2 + (self.p1[0]-self.p0[0])*2

        
    def M(self):
        return ((self.p1[0]+self.p0[0])/2, (self.p1[1]+self.p0[1])/2)
r1 = rect((0,0),(1,1))
print(r1.A())
print(r1.U())
print(r1.M())



class tri():
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.l0 = sqrt((p0[0]-p1[0])**2+(p0[1]-p1[1])**2)
        self.l1 = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        self.l2 = sqrt((p2[0]-p0[0])**2+(p2[1]-p0[1])**2)

    def A(self):
        s = self.l0 + self.l1 + self.l2