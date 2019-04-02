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

int compVerts (const void *elem1, const void *elem2) {
    if ((*((Vertex *)elem1)).order > (*((Vertex *)elem2)).order) {
        return 1;
    }
    if ((*((Vertex *)elem1)).order < (*((Vertex *)elem2)).order) {
        return -1;
    }
    return 0;
}

Object *obj_init(Vertex *t, Matrix w, int tLen) {
    Object *o = malloc(sizeof(Object));
    *o = (Object){._triangles=t, .triangles=NULL, .numTri=tLen, .World=w};
    (*o).triangles = malloc(sizeof(Vertex)*tLen);
    (*o).triangles = (Vertex *)memcpy((*o).triangles, (*o)._triangles, sizeof(Vertex)*tLen);
    (*o).numTri = tLen;
    objs = (Object *)realloc(objs, sizeof(Object)*(numObjs+1));
    *(objs+numObjs) = (*o);
    numObjs++;
    verts = (Vertex *)realloc(verts, sizeof(Vertex)*(numVerts+tLen));
    for(int n = 0; n < tLen; n++) {
        *(verts+numVerts+n) = *((*o).triangles+n);
    }
    numVerts += tLen;
    qsort(verts, numVerts, sizeof(Vertex), compVerts);
    return o;
}

void applyTransform(Object o, Matrix m) {
    o.World = matMul(m, o.World);
    for(int n = 0; n < o.numTri; n++) {
        *(o.triangles+n) = vertMul(*(o._triangles+n), o.World);
    }
    qsort(verts, numVerts, sizeof(Vertex), compVerts);
}
void Init3D(double screenRatio, double fov, double near, double far) {
    camera = translate(0, 0, 0);
    pers = perspective(fov, fov*screenRatio, far, near);
}