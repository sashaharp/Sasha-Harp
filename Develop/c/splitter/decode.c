#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void join(char* in1, char* in2, char* out, int l) {
    printf("\r\n%s\r\n", in1);
    printf("%s\r\n", in2);
    for(int n = 0; n < l; n++) {
        *(out+n) = (n%2==0) ? (*(in1 + n/2)) : (*(in2 + n/2));
    }
    printf("%s\r\n\r\n", out);
}

void unShuffle(char* arr, unsigned seed, int l) {
    int *rands = malloc(sizeof(int)*l);
    srand(seed);
    for(int n = 0; n < l; n++) {
        *(rands+n) = rand()%l;
        //printf("%i\r\n", *(rands+n));
    }
    for(int n = 0; n < l; n++) {
        char temp = *(arr+l-n-1);
        *(arr+l-n-1) = *(arr+rands[l-n-1]);
        *(arr+rands[l-n-1]) = temp;
    }
}

unsigned getSeed(char* arr2, char* arr1) {
    return ((unsigned)(*((short *)arr1))<<16) + (*((short *)arr2));
}

int main(void) {
    FILE *fp = fopen("block1", "rb");
    fseek(fp, 0L, SEEK_END);
    int l1 = ftell(fp);
    rewind(fp);
    char* arr1 = malloc(l1);
    fread(arr1, l1, 1, fp);
    fclose(fp);

    fp = fopen("block2", "rb");
    fseek(fp, 0L, SEEK_END);
    int l2 = ftell(fp);
    rewind(fp);
    char* arr2 = malloc(l2);
    fread(arr2, l2, 1, fp);
    fclose(fp);

    unsigned seed = getSeed(arr1, arr2);

    char *arr = malloc(l1+l2-4);
    printf("%s\r\n", arr2+2);
    join(arr1+2, arr2+2, arr, l1+l2-8);

    unShuffle(arr, seed, l1+l2);

    printf("seed: %#x\r\n", seed);
    printf("%s\r\n", arr);
}
