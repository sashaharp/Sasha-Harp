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

Object *obj_init(Vertex *t, Matrix w, int tLen) {
    Object *o = malloc(sizeof(Object));
    *o = (Object){._triangles=t, .triangles=NULL, .numTri=tLen, .World=w};
    (*o).triangles = malloc(sizeof(Vertex)*tLen);
	for(int n = 0; n < tLen; n++) {
		*((*o).triangles+n) = vertMul(*((*o)._triangles+n), w);
	}
    objs = (Object *)realloc(objs, sizeof(Object)*(numObjs+1));
    *(objs+numObjs) = (*o);
    numObjs++;
    verts = (Vertex *)realloc(verts, sizeof(Vertex)*(numVerts+tLen));
    for(int n = 0; n < tLen; n++) {
        *(verts+numVerts+n) = *((*o).triangles+n);
    }
    numVerts += tLen;
    return o;
}

void applyTransform(Object o, Matrix m) {
    o.World = matMul(m, o.World);
    for(int n = 0; n < o.numTri; n++) {
        *(o.triangles+n) = vertMul(*(o._triangles+n), o.World);
    }
}
void Init3D(double screenRatio, double fov, double ne, double fa) {
    camera = translate(0, 0, -50);
    pers = perspective(fov, fov*screenRatio, fa, ne);
}