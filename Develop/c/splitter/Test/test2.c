#include <stdio.h>
#include <stdlib.h>

int main(void) {
    unsigned seed;
    scanf("%x", &seed);
    printf("\r\nseed: %#x\r\n", (unsigned) seed);
    srand((unsigned) seed);
    for(int n = 0; n < 10; n++) {
        printf("%d\r\n", rand());
    }
    return 0;
}
