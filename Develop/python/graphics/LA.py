import time
import random as rand

class Vec2:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def invert(self):
        t = self.y
        self.y = self.x
        self.x = t
        return self
    def inverted(self):
        return (self.y, self.x)
    def __repr__(self):
        return (self.x, self.y)
    def __str__(self):
        return str((self.x, self.y))
    def __getitem__(self, key):
        if key:
            return self.y
        else:
            return self.x
    def __add__(self, other):
        if(str(type(other)) == "<class '__main__.Vec2'>"):
            return Vec2(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        if(str(type(other)) == "<class '__main__.Vec2'>"):
            return Vec2(self.x * other.x, self.y * other.y)
        else:
            return Vec2(self.x * other, self.y * other)

class Vec3:
    x = 0
    y = 0
    z = 0
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def invert(self):
        t = self.z
        self.z = self.x
        self.x = t
        return self
    def inverted(self):
        return (self.z, self.y, self.x)
    def __repr__(self):
        return (self.x, self.y, self.z)
    def __str__(self):
        return str((self.x, self.y, self.z))
    def __getitem__(self, key):
        return self.__repr__()[key]
    def __add__(self, other):
        if(str(type(other)) == "<class '__main__.Vec3'>"):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, other):
        if(str(type(other)) == "<class '__main__.Vec3'>"):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

class Vec4:
    x = 0
    y = 0
    z = 0
    k = 0
    def __init__(self, x, y, z, k=1):
        self.x = x
        self.y = y
        self.z = z
        self.k = k
    def invert(self):
        t = self.z
        self.z = self.y
        self.y = t
        t = self.k
        self.k = self.x
        self.x = t
        return self
    def inverted(self):
        return (self.k, self.z, self.y, self.x)
    def __repr__(self):
        return (self.x, self.y, self.z, self.k)
    def __str__(self):
        return str((self.x, self.y, self.z, self.k))
    def __getitem__(self, key):
        return self.__repr__()[key]
    def __add__(self, other):
        if(str(type(other)) == "<class '__main__.Vec4'>"):
            return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.k + other.k)
    def __mul__(self, other):
        if(str(type(other)) == "<class '__main__.Vec4'>"):
            return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.k * other.k)
        else:
            return Vec4(self.x * other, self.y * other, self.z * other, self.k * other)

class VecN:
    def __init__(self, *dims):
        if(str(type(dims[0])) == "<class 'list'>"):
            self.dims = dims[0]
        else:
            self.dims = list(dims)
    def invert(self):
        self.dims = self.dims[::-1]
        return self
    def inverted(self):
        return self.__repr__()[::-1]
    def __repr__(self):
        return self.dims
    def __str__(self):
        return str(self.dims)
    def __getitem__(self, key):
        return self.dims[key]
    def __add__(self, other):
        if(str(type(other)) == "<class '__main__.VecN'>"):
            t = list(self.dims)
            for pn, n in enumerate(other.dims):
                t[pn] += n
            return VecN(t)
    def __mul__(self, other):
        if(str(type(other)) == "<class '__main__.VecN'>"):
            t = list(self.dims)
            for pn, n in enumerate(other.dims):
                t[pn] *= n
            return VecN(t)
        else:
            t = list(self.dims)
            for n in range(len(self)):
                t[n] *= other
            return VecN(t)
    def __setitem__(self, key, value):
        self.dims[key] = value

class Mat2x2:
    def __init__(self, x11, x12, x21, x22):
        self.x11 = x11
        self.x12 = x12
        self.x21 = x21
        self.x22 = x22
    def __getitem__(self, key):
        if key == 0:
            return [self.x11, self.x12]
        elif key == 1:
            return [self.x21, self.x22]
        else:
            return None
    def __repr__(self):
        return [[self.x11, self.x12],[self.x21, self.x22]]
    def __str__(self):
        l1 = len(str(self.x11))
        l2 = len(str(self.x21))
        return str(self.x11) + " "*(max(0, l2-l1)) + ", " + str(self.x12) + "\n" + str(self.x21) + " "*(max(0, l1-l2)) + ", "  + str(self.x22)
    def __mul__(self, other):
        if(str(type(other)) == "<class '__main__.Mat2x2'>"):
            return Mat2x2(self.x11*other.x11+self.x12*other.x21,  self.x11*other.x12+self.x12*other.x22,
                self.x21*other.x11+self.x22*other.x21,  self.x21*other.x12+self.x22*other.x22)
        elif(str(type(other)) != "<class '__main__.Vec2'>"):
            return Vec2(self.x11 * other.x + self.x12 * other.y, self.x21 * other.x + self.x22 * other.y)
        else:
            return Mat2x2(self.x11 * other, self.x12 * other, self.x21 * other, self.x22 * other)
    def __rmul__(self, other):
        if(str(type(other)) == "<class 'int'>"):
            return Mat2x2(self.x11 * other, self.x12 * other, self.x21 * other, self.x22 * other)

class Mat3x3:
    def __init__(self, x11, x12, x13, x21 = None, x22 = None, x23 = None, x31 = None, x32 = None, x33 = None):
        if x21 is not None:
            self.x11 = x11
            self.x12 = x12
            self.x13 = x13
            self.x21 = x21
            self.x22 = x22
            self.x23 = x23
            self.x31 = x31
            self.x32 = x32
            self.x33 = x33
        else:
            self.x11 = x11[0]
            self.x12 = x11[1]
            self.x13 = x11[2]
            self.x21 = x12[0]
            self.x22 = x12[1]
            self.x23 = x12[2]
            self.x31 = x13[0]
            self.x32 = x13[1]
            self.x33 = x13[2]
    def __getitem__(self, key):
        if key == 0:
            return [self.x11, self.x12, self.x13]
        elif key == 1:
            return [self.x21, self.x22, self.x23]
        elif key == 2:
            return [self.x31, self.x32, self.x33]
        else:
            return None
    def __repr__(self):
        return [[self.x11, self.x12, self.x13],[self.x21, self.x22, self.x23],[self.x31, self.x32, self.x33]]
    def __str__(self):
        l1 = max(len(str(self.x11)),len(str(self.x21)),len(str(self.x31)))
        l2 = max(len(str(self.x12)),len(str(self.x22)),len(str(self.x32)))
        return (str(self.x11) 
            + " "*(l1-len(str(self.x11))) 
            + ", " + str(self.x12) 
            + " "*(l2-len(str(self.x12))) 
            + ", " + str(self.x13) 
            + "\n" + str(self.x21) 
            + " "*(l1-len(str(self.x21)))
            + ", "  + str(self.x22)
            + " "*(l2-len(str(self.x22)))
            + ", "  + str(self.x23)
            + "\n" + str(self.x31) 
            + " "*(l1-len(str(self.x31)))
            + ", "  + str(self.x32)
            + " "*(l2-len(str(self.x32)))
            + ", "  + str(self.x33))
    def __mul__(self, other):
        if(str(type(other)) == "<class '__main__.Mat3x3'>"):
            return Mat3x3(
                self.x11*other.x11+self.x12*other.x21+self.x13*other.x31,   self.x11*other.x12+self.x12*other.x22+self.x13*other.x32,   self.x11*other.x13+self.x12*other.x23+self.x13*other.x33,
                self.x21*other.x11+self.x22*other.x21+self.x23*other.x31,   self.x21*other.x12+self.x22*other.x22+self.x23*other.x32,   self.x21*other.x13+self.x22*other.x23+self.x23*other.x33,
                self.x31*other.x11+self.x32*other.x21+self.x33*other.x31,   self.x31*other.x12+self.x32*other.x22+self.x33*other.x32,   self.x31*other.x13+self.x32*other.x23+self.x33*other.x33
            )
        elif(str(type(other)) != "<class '__main__.Vec3'>"):
            return Vec3(self.x11 * other.x + self.x12 * other.y + self.x13 * other.z, 
                        self.x21 * other.x + self.x22 * other.y + self.x23 * other.z,
                        self.x31 * other.x + self.x32 * other.y + self.x33 * other.z)
        else:
            return Mat3x3(
                self.x11 * other, self.x12 * other, self.x13 * other,
                self.x21 * other, self.x22 * other, self.x23 * other,
                self.x31 * other, self.x32 * other, self.x33 * other)
    def __rmul__(self, other):
        if(str(type(other)) == "<class 'int'>"):
            return Mat3x3(
                self.x11 * other, self.x12 * other, self.x13 * other,
                self.x21 * other, self.x22 * other, self.x23 * other,
                self.x31 * other, self.x32 * other, self.x33 * other)
        
class Mat4x4:
    def __init__(self, x11, x12, x13, x14, x21 = None, x22 = None, x23 = None, x24 = None, x31 = None, x32 = None, x33 = None, x34 = None, x41 = None, x42 = None, x43 = None, x44 = None):
        if x21 is not None:
            self.x11 = x11
            self.x12 = x12
            self.x13 = x13
            self.x14 = x14
            self.x21 = x21
            self.x22 = x22
            self.x23 = x23
            self.x24 = x24
            self.x31 = x31
            self.x32 = x32
            self.x33 = x33
            self.x34 = x34
            self.x41 = x41
            self.x42 = x42
            self.x43 = x43
            self.x44 = x44
        else:
            self.x11 = x11[0]
            self.x12 = x11[1]
            self.x13 = x11[2]
            self.x14 = x11[3]
            self.x21 = x12[0]
            self.x22 = x12[1]
            self.x23 = x12[2]
            self.x24 = x12[3]
            self.x31 = x13[0]
            self.x32 = x13[1]
            self.x33 = x13[2]
            self.x34 = x13[3]
            self.x41 = x14[0]
            self.x42 = x14[1]
            self.x43 = x14[2]
            self.x44 = x14[3]
    def __getitem__(self, key):
        if key == 0:
            return [self.x11, self.x12, self.x13, self.x14]
        elif key == 1:
            return [self.x21, self.x22, self.x23, self.x24]
        elif key == 2:
            return [self.x31, self.x32, self.x33, self.x34]
        elif key == 3:
            return [self.x41, self.x42, self.x43, self.x44]
        else:
            raise IndexError
    def __repr__(self):
        return [[self.x11, self.x12, self.x13, self.x14],[self.x21, self.x22, self.x23, self.x24],[self.x31, self.x32, self.x33, self.x34],[self.x41, self.x42, self.x43, self.x44]]
    def __str__(self):
        l1 = max(len(str(self.x11)),len(str(self.x21)),len(str(self.x31), len(str(self.x41))))
        l2 = max(len(str(self.x12)),len(str(self.x22)),len(str(self.x32), len(str(self.x42))))
        l3 = max(len(str(self.x13)),len(str(self.x23)),len(str(self.x33), len(str(self.x43))))
        return (str(self.x11) 
            + " "*(l1-len(str(self.x11))) 
            + ", " + str(self.x12) 
            + " "*(l2-len(str(self.x12))) 
            + ", " + str(self.x13) 
            + " "*(l3-len(str(self.x13))) 
            + ", " + str(self.x14) 
            + "\n" + str(self.x21) 
            + " "*(l1-len(str(self.x21)))
            + ", "  + str(self.x22)
            + " "*(l2-len(str(self.x22)))
            + ", "  + str(self.x23)
            + " "*(l3-len(str(self.x23)))
            + ", "  + str(self.x24)
            + "\n" + str(self.x31) 
            + " "*(l1-len(str(self.x31)))
            + ", "  + str(self.x32)
            + " "*(l2-len(str(self.x32)))
            + ", "  + str(self.x33)
            + " "*(l3-len(str(self.x34)))
            + ", "  + str(self.x34)
            + "\n" + str(self.x41) 
            + " "*(l1-len(str(self.x41)))
            + ", "  + str(self.x42)
            + " "*(l2-len(str(self.x42)))
            + ", "  + str(self.x43)
            + " "*(l3-len(str(self.x44)))
            + ", "  + str(self.x44))
    def __mul__(self, other):
        if(str(type(other)) == "<class '__main__.Mat4x4'>"):
            return Mat4x4(
                self.x11*other.x11+self.x12*other.x21+self.x13*other.x31,   self.x11*other.x12+self.x12*other.x22+self.x13*other.x32,   self.x11*other.x13+self.x12*other.x23+self.x13*other.x33,
                self.x21*other.x11+self.x22*other.x21+self.x23*other.x31,   self.x21*other.x12+self.x22*other.x22+self.x23*other.x32,   self.x21*other.x13+self.x22*other.x23+self.x23*other.x33,
                self.x31*other.x11+self.x32*other.x21+self.x33*other.x31,   self.x31*other.x12+self.x32*other.x22+self.x33*other.x32,   self.x31*other.x13+self.x32*other.x23+self.x33*other.x33,
                self.x41*other.x11+self.x42*other.x21+self.x43*other.x31,   self.x41*other.x12+self.x42*other.x22+self.x43*other.x32,   self.x41*other.x13+self.x42*other.x23+self.x43*other.x33
            )
        elif(str(type(other)) != "<class '__main__.Vec4'>"):
            return Vec4(self.x11 * other.x + self.x12 * other.y + self.x13 * other.z + self.x14 * other.k, 
                        self.x21 * other.x + self.x22 * other.y + self.x23 * other.z + self.x24 * other.k,
                        self.x31 * other.x + self.x32 * other.y + self.x33 * other.z + self.x34 * other.k,
                        self.x41 * other.x + self.x42 * other.y + self.x43 * other.z + self.x44 * other.k)
        else:
            return Mat4x4(
                self.x11 * other, self.x12 * other, self.x13 * other, self.x14 * other,
                self.x21 * other, self.x22 * other, self.x23 * other, self.x24 * other,
                self.x31 * other, self.x32 * other, self.x33 * other, self.x34 * other,
                self.x41 * other, self.x42 * other, self.x43 * other, self.x44 * other)
    def __rmul__(self, other):
        if(str(type(other)) == "<class 'int'>"):
            return Mat4x4(
                self.x11 * other, self.x12 * other, self.x13 * other, self.x14 * other,
                self.x21 * other, self.x22 * other, self.x23 * other, self.x24 * other,
                self.x31 * other, self.x32 * other, self.x33 * other, self.x34 * other,
                self.x41 * other, self.x42 * other, self.x43 * other, self.x44 * other)
        
class quaternion(object):
    def __init__(self, n, i, j, k):
        self.n = n
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        if isinstance(other, int):
            return quaternion(self.n + other, self.i, self.j, self.k)
        if isinstance(other, complex):
            return quaternion(self.n + other.real, self.i + other.imag, self.j, self.k)
        if isinstance(other, quaternion):
            return quaternion(self.n+other.n, self.i + other.i, self.j + other.j, self.k + other.k)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, quaternion):
            return quaternion(self.n*other.n-self.i*other.i-self.j*other.j-self.k*other.k, self.n*other.i+other.n*self.i+self.j*other.k-self.k*other.j, self.n*other.j+other.n*self.j+self.k*other.i-self.i*other.k, self.n*other.k+other.n*self.k+self.i*other.j-self.j*other.i)
        if isinstance(other, int):
            return quaternion(self.n * other, self.i * other, self.j * other, self.k * other)
        if isinstance(other, complex):
            temp = quaternion(other.real, other.imag, 0, 0)
            return self * temp
        return NotImplemented

    def __rmul(self, other):
        if isinstance(other, int):
            return self*other
        return NotImplemented

        


def runnC():
    vec1 = VecN(123, 456, 789)
    vec2 = VecN(321, 654, 987)
    vec3 = vec1 + vec2
    vec4 = vec1 * vec2
    vec4.invert()
    print(vec1)
    print(vec2)
    print(vec3)
    print(vec4)
    
    

time.clock()

vec = Vec2(10, 11)
mat = Mat3x3(2, 2000, 1, 2000, 0, 1, 0, 0, 1)
#mat = 2 * mat
n = mat * vec
print(mat)



print(time.clock())