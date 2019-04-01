#include "3dStructs.h"

typedef struct _Object {
    Vertex *_triangles;
    Vertex *triangles;
    int numTri;
    Matrix World;
} Object;

Object *objs;
int numObjs;
Vertex *verts;
int numVerts;
Matrix camera;
Matrix pers;


Object obj(Vertex *t, Matrix w, int tLen) {
    Object o = {._triangles=t, .triangles=NULL, .numTri=tLen, .World=w};
    memcpy(o.triangles, o._triangles, sizeof(*o._triangles)*tLen);
    o.numTri = tLen;
    
    return o;
}

void applyTransform(Object o, Matrix m) {
    o.World = matMul(m, o.World);
    for(int n = 0; n < o.numTri; n++) {
        *(o.triangles+n) = vertMul(*(o._triangles+n), o.World);
    }
}
void Init3D(double screenRatio, double fov, double near, double far) {
    camera = translate(0, 0, 0);
    pers = perspective(fov, fov*screenRatio, far, near);
}

void putObj(Object o) {
    objs = (Object *)realloc(objs, sizeof(Object)*(numObjs+1));
    *(objs+numObjs) = o;
    numObjs++;
    verts = (Vertex *)realloc(verts, sizeof(Vertex)*(numVerts+o.numTri));
    for(int n = numVerts; n < numVerts + o.numTri; n++) {
        *(verts+n) = *(o.triangles+n);
    }
    numVerts += o.numTri;
}