#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int swap(int num) {
    return ((num>>24)&0xff) | // move byte 3 to byte 0
                    ((num<<8)&0xff0000) | // move byte 1 to byte 2
                    ((num>>8)&0xff00) | // move byte 2 to byte 1
                    ((num<<24)&0xff000000);
}

short swapshort(short num) {
    return (num>>8) | (num<<8);
}

char *compressionlookup(int compnum) {
    switch (compnum)
    {
        case 0:
            return "BI_RGB (no compression)";
        case 1:
            return "BI_RLE8 (RLE 8-bit/pixel)";
        case 2:
            return "BI_RLE4 (RLE 4-bit/pixel)";
        case 3:
            return "BI_BITFIELDS (OS22XBITMAPHEADER: Huffman 1D)";
        case 4:
            return "BI_JPEG (OS22XBITMAPHEADER: RLE-24)";
        case 5:
            return "BI_PNG ()";
        case 6:
            return "BI_ALPHABITFIELDS (RGBA bit field masks)";
        case 11:
            return "BI_CMYK (no compression)";
        case 12:
            return "BI_CMYKRLE8 (RLE-8)";
        case 13:
            return "BI_CMYKRLE4 (RLE-4)";  
        default: ;
            char *buffer;
            buffer = malloc(200);
            sprintf(buffer, "unknown compression (number: %d)", compnum);
            return buffer;
    }
}

char *tb(char c) {
    char *buffer = malloc(8);
    strcpy(buffer, "00000000");
    if(c&0b10000000) {
        *buffer = '1';
    }
    if(c&0b01000000) {
        *(buffer+1) = '1';
    }
    if(c&0b00100000) {
        *(buffer+2) = '1';
    }
    if(c&0b00010000) {
        *(buffer+3) = '1';
    }
    if(c&0b00001000) {
        *(buffer+4) = '1';
    }
    if(c&0b00000100) {
        *(buffer+5) = '1';
    }
    if(c&0b00000010) {
        *(buffer+6) = '1';
    }
    if(c&0b00000001) {
        *(buffer+7) = '1';
    }
    return buffer;
}

int main() {
    FILE *fp;
    if((fp = fopen("test.bmp", "rb"))==NULL) {
        printf("panic\n");
        return -1;
    }
    char *fileheader = malloc(sizeof(char) * 14);
    fgets(fileheader, 14, fp);
    printf("%c%c\n", *fileheader, *(fileheader+1));
    printf("BM magic size: %d\n", *(int *)(fileheader+2));
    printf("Two offsets, should be zero: %d, %d\n", *(short *)(fileheader+6), *(short *)(fileheader+8));
    printf("Offset to image: %d\n", *(int *)(fileheader+10));
    printf("______________________________________________________________\n\n");

    char *imageheader = malloc(sizeof(char) * (*(int *)(fileheader+10) - 14));
    fgets(imageheader, *(int *)(fileheader+10) - 14, fp);
    printf("Header Size: %d\n", *(int *)(imageheader));
    printf("Dimentions: %d x %d\n", *(int *)(imageheader+4), *(int *)(imageheader+8) );
    printf("Number of color planes: %d (must be one, sooo... bs?)\n", swapshort(*(short *)(imageheader+12)) );
    printf("Size of the pixel: %d\n", swapshort(*(short *)(imageheader+14)) );
    printf("Compression method: %s\n", compressionlookup(swap(*(int *)(imageheader+16))));
    printf("Size of the raw image data (could be 0 for BI_RGB): %d\n", swap(*(int *)(imageheader+20)));
    printf("Resolution: %d x %d\n", *(int *)(imageheader+24), *(int *)(imageheader+28));
    printf("Amount of colours in Pallette: %d\n", swap(*(int *)(imageheader+32)));
    printf("Amount of important colours: %d\n", swap(*(int *)(imageheader+36)));
    
    printf("______________________________________________________________\n\n");
    printf("Colour-map:\n");
    for(int n = 0; n < swap(*(int *)(imageheader+32)) * 4; n++) {
        if((unsigned char)*(imageheader+40+n)>99) {
            printf("%d ", (unsigned char)*(imageheader+40+n));
        } else if((unsigned char)*(imageheader+40+n)>9){
            printf("%d  ", (unsigned char)*(imageheader+40+n));
        } else {
            printf("%d   ", (unsigned char)*(imageheader+40+n));
        }
        if(n%16==15) {
            printf("\n");
        }else if(n%4==3) {
            printf(", ");
        }
    }
    printf("%d / %ld\n", 14+40+swap(*(int *)(imageheader+32)) * 4, sizeof(char) * (*(int *)(fileheader+10)));
    
    printf("______________________________________________________________\n\n");
    char *image = malloc(sizeof(char) * *(int *)(imageheader+4) * *(int *)(imageheader+8));
    fgets(image, *(int *)(imageheader+4) * *(int *)(imageheader+8), fp);
    printf("image:\n");
    //swap(*(int *)(imageheader+4)) * swap(*(int *)(imageheader+8))
    for(int n = 0; n < 2000; n++) {
        printf("%02x  ", (unsigned char)*(image+n));
        
        if(n%32==31) {
            printf("\n");
        }
    }
    return 0;
}