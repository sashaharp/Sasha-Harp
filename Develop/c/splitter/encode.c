#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

unsigned getSeed() {
    time_t t;
    time(&t);
    srand((unsigned) t);
    return rand(); 
}

void shuffle(char* arr, unsigned seed, int length) {
    srand(seed);
    for(int n = 0; n < length; n++) {
        char temp = *(arr + n);
        int r = rand() % length;
        printf("%i\r\n", r);
        *(arr + n) = *(arr + r);
        *(arr + r) = temp;
    }
}

void split(char* arr, char* out1, char* out2, int length) {
    for(int n = 0; n < length; n++) {
        if(n%2 == 0) {
            *(out1 + n/2) = *(arr+n);
        } else {
            *(out2 + (n-1)/2) = *(arr+n);
        }
    }
}

int main(void) {
    unsigned seed = getSeed();
    printf("seed: %#x\r\n", seed);

    FILE *fp = fopen("test", "rb");
    fseek(fp, 0L, SEEK_END);
    int l = ftell(fp);
    rewind(fp);
    char* arr = malloc(l);
    fread(arr, l, 1, fp);
    fclose(fp);

    printf("initial data: %s\r\n", arr);
    shuffle(arr, seed, l);
    printf("shuffeled data: %s\r\n", arr);
    
    char* out1 = malloc(l/2 + l%2 + 2);
    char* out2 = malloc(l/2 + 2);
    split(arr, out1+2, out2+2, l);
    free(arr);
    *((short *)out1) = *(short *)(&seed);
    *((short *)out2) = *((short *)(&seed) + 1);

    fp = fopen("block1", "wb");
    fwrite(out1, l/2 + l%2 + 2, 1, fp);
    fp = fopen("block2", "wb");
    fwrite(out2, l/2 + 2, 1, fp);
    //printf("first datablock: %s\r\n", out1);
    //printf("second datablock: %s\r\n", out2);
    //printf("test: %#x", ((unsigned)(*((short *)out2))<<16) + (*((short *)out1)));
}