#include <math.h>
#include <stdlib.h>
#include <string.h>
#include "TextureStruct.h"

typedef struct _Vector {
    double x;
    double y;
    double z;
    double w;
} Vector;

Vector vect(double x, double y, double z) {
    Vector v = {.x = x, .y = y, .z = z, .w = 1};
    return v;
}

typedef struct _Vertex {
    Vector v1;
    Vector v2;
    Vector v3;
	Texture col;
} Vertex;

Vertex vert(Vector v1, Vector v2, Vector v3, Texture t) {
    Vertex v = {.v1 = v1, .v2 = v2, .v3 = v3, .col = t};
    return v;
}

typedef struct _Matrix {
    double m11;
    double m12;
    double m13;
    double m14;
    
    double m21;
    double m22;
    double m23;
    double m24;
    
    double m31;
    double m32;
    double m33;
    double m34;
    
    double m41;
    double m42;
    double m43;
    double m44;
} Matrix;

Matrix rotateX (double phi) {
    double sinPhi = sin(phi);
    double cosPhi = cos(phi);
    Matrix m = {.m11 = 1, .m12 = 0, .m13 = 0, .m14 = 0,
                .m21 = 0, .m22 = cosPhi, .m23 = -sinPhi, .m24 = 0,
                .m31 = 0, .m32 = sinPhi, .m33 = cosPhi, .m34 = 0,
                .m41 = 0, .m42 = 0, .m43 = 0, .m44 = 1};
    return m;
}

Matrix rotateY (double phi) {
    double sinPhi = sin(phi);
    double cosPhi = cos(phi);
    Matrix m = {.m11 = cosPhi, .m12 = 0, .m13 = sinPhi, .m14 = 0,
                .m21 = 0, .m22 = 1, .m23 = 0, .m24 = 0,
                .m31 = -sinPhi, .m32 = 0, .m33 = cosPhi, .m34 = 0,
                .m41 = 0, .m42 = 0, .m43 = 0, .m44 = 1};
    return m;
}

Matrix rotateZ (double phi) {
    double sinPhi = sin(phi);
    double cosPhi = cos(phi);
    Matrix m = {.m11 = cosPhi, .m12 = -sinPhi, .m13 = 0, .m14 = 0,
                .m21 = sinPhi, .m22 = cosPhi, .m23 = 0, .m24 = 0,
                .m31 = 0, .m32 = 0, .m33 = 1, .m34 = 0,
                .m41 = 0, .m42 = 0, .m43 = 0, .m44 = 1};
    return m;
}

Matrix translate (double x, double y, double z) {
    Matrix m = {.m11=1, .m12=0, .m13=0, .m14=x,
                .m21=0, .m22=1, .m23=0, .m24=y,
                .m31=0, .m32=0, .m33=1, .m34=z,
                .m41=0, .m42=0, .m43=0, .m44=1};
    return m;
}

Matrix perspective (double fovX, double fovY, double fa, double ne) {
    double Sx = 1/tan(fovX*M_PI/360);
    double Sy = 1/tan(fovY*M_PI/360);
    Matrix m = {.m11 = Sx, .m12 = 0, .m13 = 0, .m14 = 0,
                .m21 = 0, .m22 = Sy, .m23 = 0, .m24 = 0,
                .m31 = 0, .m32 = 0, .m33 = -fa/(fa-ne), .m34 = -1,
                .m41 = 0, .m42 = 0, .m43 = -fa*ne/(fa-ne), .m44 = 0};
    return m;
}

Matrix matMul (Matrix a, Matrix b) {
    Matrix m = {a.m11*b.m11 + a.m12*b.m21 + a.m13*b.m31 + a.m14*b.m41,
                a.m11*b.m12 + a.m12*b.m22 + a.m13*b.m32 + a.m14*b.m42,
                a.m11*b.m13 + a.m12*b.m23 + a.m13*b.m33 + a.m14*b.m43,
                a.m11*b.m14 + a.m12*b.m24 + a.m13*b.m34 + a.m14*b.m44,
                
                a.m21*b.m11 + a.m22*b.m21 + a.m23*b.m31 + a.m24*b.m41,
                a.m21*b.m12 + a.m22*b.m22 + a.m23*b.m32 + a.m24*b.m42,
                a.m21*b.m13 + a.m22*b.m23 + a.m23*b.m33 + a.m24*b.m43,
                a.m21*b.m14 + a.m22*b.m24 + a.m23*b.m34 + a.m24*b.m44,
                
                a.m31*b.m11 + a.m32*b.m21 + a.m33*b.m31 + a.m34*b.m41,
                a.m31*b.m12 + a.m32*b.m22 + a.m33*b.m32 + a.m34*b.m42,
                a.m31*b.m13 + a.m32*b.m23 + a.m33*b.m33 + a.m34*b.m43,
                a.m31*b.m14 + a.m32*b.m24 + a.m33*b.m34 + a.m34*b.m44,
                
                a.m41*b.m11 + a.m42*b.m21 + a.m43*b.m31 + a.m44*b.m41,
                a.m41*b.m12 + a.m42*b.m22 + a.m43*b.m32 + a.m44*b.m42,
                a.m41*b.m13 + a.m42*b.m23 + a.m43*b.m33 + a.m44*b.m43,
                a.m41*b.m14 + a.m42*b.m24 + a.m43*b.m34 + a.m44*b.m44};
    return m;
}

Vector vectMul (Vector a, Matrix m) {
    double w = m.m41*a.x + m.m42*a.y + m.m43*a.z + m.m44*a.w;
    Vector v = vect((m.m11*a.x + m.m12*a.y + m.m13*a.z + m.m14*a.w)/w,
                    (m.m21*a.x + m.m22*a.y + m.m23*a.z + m.m24*a.w)/w,
                    (m.m31*a.x + m.m32*a.y + m.m33*a.z + m.m34*a.w)/w); 
    return v;
}

Vertex vertMul (Vertex a, Matrix m) {
    Vertex v = vert(vectMul(a.v1, m), vectMul(a.v2, m), vectMul(a.v3, m), a.col);
    return v;
}