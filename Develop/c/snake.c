#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define true 1
#define false 0

short player;
short dplayer;
char looping;
char *field;

void *inputloop(void *vargp) {
    do {
        char c = getchar();
        if (c == 'x') {
            looping = false;
        } else if (c == 'w') {
            dplayer = 0x0001;
        } else if (c == 's') {
            dplayer = 0x0201;
        } else if (c == 'a') {
            dplayer = 0x0100;
        } else if (c == 'd') {
            dplayer = 0x0102;
        }
    } while (looping);
}

void draw() {
    printf("\e[1;1H\e[2J");
    for(int n = 0; n < 24*80-1; n+=1) {
        *(field+n) = ' ';
    }

    *(field + *(char *)&player + *((char *)&player+1)*80) = '#';

    printf("%s",field);
}

void update() {
    player += dplayer-0x0101;
}

int main() {
    /*
    long t = 0x0A21214F4C4C4548;
    
    for(int n = 0; n < 8; n+=1) {
        printf("%c", *((char *)&t+n) );
    }*/
    looping = true;
    dplayer = 0x0101;
    *((char *)&player) = 39;
    *((char *)&player+1) = 11;
    field = malloc(sizeof(char)*24*80-1);
    
    pthread_t thread_id;
    pthread_create(&thread_id, NULL, inputloop, NULL);

    do {
        draw();
        update();
        sleep(5);
    } while (looping);

    return 0;
}