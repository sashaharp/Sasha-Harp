#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gmtl/gmtl.h>
#include <gmtl/Vec.h>


double perlin(double x, double y) {

    //separation into unit squares:
    double xx = x-trunc(x);
    double yy = y-trunc(y);

    //generate vectors
    gmtl::Vec<double, 2> v1 = gmtl::Vec<double, 2>(double(rand()%3-1)/2, double(rand()%3-1)/2);
    gmtl::Vec<double, 2> v2 = gmtl::Vec<double, 2>(double(rand()%3-1)/2, double(rand()%3-1)/2);
    gmtl::Vec<double, 2> v3 = gmtl::Vec<double, 2>(double(rand()%3-1)/2, double(rand()%3-1)/2);
    gmtl::Vec<double, 2> v4 = gmtl::Vec<double, 2>(double(rand()%3-1)/2, double(rand()%3-1)/2);

    gmtl::Vec<double, 2> vv1 = gmtl::Vec<double, 2>(xx-0, yy-1);//1--2
    gmtl::Vec<double, 2> vv2 = gmtl::Vec<double, 2>(xx-1, yy-1);//|  |
    gmtl::Vec<double, 2> vv3 = gmtl::Vec<double, 2>(xx-1, yy-0);//4--3
    gmtl::Vec<double, 2> vv4 = gmtl::Vec<double, 2>(xx-0, yy-0);

    //dot products
    double d1 = v1[0]*vv1[0]+v1[1]*vv1[1];
    double d2 = v2[0]*vv2[0]+v2[1]*vv2[1];
    double d3 = v3[0]*vv3[0]+v3[1]*vv3[1];
    double d4 = v4[0]*vv4[0]+v4[1]*vv4[1];

    //lerp
    double x1 = d1+xx*(d2-d1);
    double x2 = d4+xx*(d3-d4);

    double av = x2+yy*(x1-x2);

    //return
    return av;
}

int main(void) {
    //rand
    time_t t;
    time(&t);
    srand((unsigned) t);
    FILE *fp = fopen("result", "wb");
    for(double i = 0.0; i < 10.0; i += 0.005) {
        for(double j = 0.0; j < 10.0; j += 0.005) {
            double p = perlin(j, i);
            char *s_p = (char *)malloc(6);
            sprintf(s_p, "%+.2f;", p);
            fwrite(s_p, 6, 1, fp);
        }
        fwrite("\n", 1, 1, fp);
    }
    return 0;
}

