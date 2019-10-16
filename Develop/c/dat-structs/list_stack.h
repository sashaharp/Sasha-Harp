#include <stdlib.h>

struct listElement {
    int val;
    struct listElement *next;
} list_init = {0, NULL};

char list_push(struct listElement* head, int val) {
    struct listElement* newEl = (struct listElement *)malloc(sizeof(struct listElement));
    (*newEl).val = val;
    (*newEl).next = (*head).next;
    (*head).next = newEl;
    return 1;
}

char list_pop(struct listElement* head, int *val) {
    if((*head).next == NULL) {
        return -1;
    }
    *val = (*(*head).next).val;
    struct listElement* temp = (*(*head).next).next;
    free((void *)(*head).next);
    (*head).next = temp;
    return 1;
}

char list_isEmpty(struct listElement* head) {
    return (*head).next == NULL;
}