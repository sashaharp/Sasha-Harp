#include <stdio.h>
#include <stdlib.h>

#include "list_stack.h"

int main() {
    struct listElement head = list_init;
    struct listElement second_head = list_init;
    list_push(&head, 2);
    list_push(&head, 3);
    list_push(&second_head, 4);
    list_push(&second_head, 5);
    int v;
    list_pop(&head, &v);
    printf("fh: %d\n", v);
    list_pop(&second_head, &v);
    printf("sh: %d\n", v);
    list_pop(&head, &v);
    printf("fh: %d\n", v);
    list_pop(&second_head, &v);
    printf("sh: %d\n", v);
    printf("fh: %d\n", list_isEmpty(&head));
    printf("sh: %d", list_isEmpty(&second_head));
    return 1;
}