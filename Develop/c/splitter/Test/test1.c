#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void) {
    time_t t;
    time(&t);
    srand((unsigned) t);
    printf("seed: %#x\r\n", (unsigned) t);
    for(int n = 0; n < 10; n++) {
        printf("%d\r\n", rand());
    }
    return 0;
}
