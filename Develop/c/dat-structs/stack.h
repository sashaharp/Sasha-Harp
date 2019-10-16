#include <stdlib.h>
#define STACK_MAX 254

struct stack {
    unsigned char n;
    int vals[255];
};

char stack_push(struct stack* s, int val) {
    if((*s).n <= STACK_MAX) {
        (*s).vals[(*s).n] = val;
        (*s).n++;
        return 0;
    }
    return -1;
}

char stack_pop(struct stack* s, int* val) {
    if((*s).n > 0) {
        *val = (*s).vals[(*s).n-1];
        (*s).n--;
        return 0;
    }
    return -1;
}

char isEmpty(struct stack* s) {
    return (*s).n == 0;
}