#include <windows.h>

//<win32>
typedef struct _Texture {
    char kind;
	COLORREF c;
    COLORREF *cs;
    COLORREF **csa;
} Texture;
//</win32>