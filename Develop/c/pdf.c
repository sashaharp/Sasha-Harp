#include <stdio.h>
#include <stdlib.h>

unsigned char reverse(unsigned char b) {
   b = (b & 0xF0) >> 4 | (b & 0x0F) << 4;
   b = (b & 0xCC) >> 2 | (b & 0x33) << 2;
   b = (b & 0xAA) >> 1 | (b & 0x55) << 1;
   return b;
}

void main() {
    FILE *fp = fopen("test1.pdf", "rb");
    char *content = malloc(sizeof(char) * 8);
    char *eight = malloc(sizeof(char) * 7);
    for (int n = 0; n < 50; n++) {
        int n = 0;
        while ( ((*(eight+n))=fgetc(fp))!= EOF && n < 8 ) {
            n++;
        }
        *content = reverse((*eight&0b11111110)>>1);
        *(content+1) = reverse((*(eight+1)&0b11111100)>>2 + (*eight&0b00000001)<<6);
        *(content+2) = reverse((*(eight+2)&0b11111000)>>3 + (*(eight+1)&0b00000011)<<5);
        *(content+3) = reverse((*(eight+3)&0b11110000)>>4 + (*(eight+2)&0b00000111)<<4);
        *(content+4) = reverse((*(eight+4)&0b11100000)>>5 + (*(eight+3)&0b00001111)<<3);
        *(content+5) = reverse((*(eight+5)&0b11000000)>>6 + (*(eight+4)&0b00011111)<<2);
        *(content+6) = reverse((*(eight+6)&0b10000000)>>7 + (*(eight+5)&0b00111111)<<1);
        *(content+7) = reverse((*(eight+6)&0b01111111));
        printf("%s", content);
        printf("\n");
    }
}