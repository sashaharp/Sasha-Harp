#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdio.h>
#include "3dRender.h"


//http://www.winprog.org/tutorial/simple_window.html

const char g_szClassName[] = "myWindowClass";

COLORREF *field;

double area(double x1, double y1, double x2, double y2, double x3, double y3) {
	return fabs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2.0;
}

char inVertex(Vertex v, double x, double y) {
	double A  = area(v.v1.x, v.v1.y, v.v2.x, v.v2.y, v.v3.x, v.v3.y);
	double A1 = area(x     , y     , v.v2.x, v.v2.y, v.v3.x, v.v3.y);
	double A2 = area(v.v1.x, v.v1.y, x     , y     , v.v3.x, v.v3.y);
	double A3 = area(v.v1.x, v.v1.y, v.v2.x, v.v2.y, x     , y     );
	return fabs(A - (A1 + A2 + A3))<0.000000001;
}

void gen() {
    Vector points[8];
    points[0] = vect(-0.5, -0.5, -0.5);
    points[1] = vect(-0.5,  0.5, -0.5);
    points[2] = vect( 0.5,  0.5, -0.5);
    points[3] = vect( 0.5, -0.5, -0.5);
    points[4] = vect(-0.5, -0.5,  0.5);
    points[5] = vect(-0.5,  0.5,  0.5);
    points[6] = vect( 0.5,  0.5,  0.5);
    points[7] = vect( 0.5, -0.5,  0.5);

    Vertex verts[12];
    verts[0] = vert(points[0], points[1], points[2], (Texture){RGB(100, 100, 0)});
    verts[1] = vert(points[0], points[2], points[3], (Texture){RGB(100, 100, 0)});
    
    verts[2] = vert(points[4], points[5], points[6], (Texture){RGB(100, 0, 100)});
    verts[3] = vert(points[4], points[6], points[7], (Texture){RGB(100, 0, 100)});
    
    verts[4] = vert(points[0], points[1], points[5], (Texture){RGB(0, 100, 100)});
    verts[5] = vert(points[0], points[5], points[4], (Texture){RGB(0, 100, 100)});
    
    verts[6] = vert(points[3], points[2], points[6], (Texture){RGB(100, 0, 0)});
    verts[7] = vert(points[3], points[6], points[7], (Texture){RGB(100, 0, 0)});
    
    verts[8] = vert(points[1], points[2], points[6], (Texture){RGB(0, 100, 0)});
    verts[9] = vert(points[1], points[6], points[5], (Texture){RGB(0, 100, 0)});
    
    verts[10] = vert(points[0], points[1], points[7], (Texture){RGB(0, 0, 100)});
    verts[11] = vert(points[0], points[7], points[4], (Texture){RGB(0, 0, 100)});
    
    Object *o = obj_init(verts, matMul(rotateY(0), rotateX(0)), 12);
}

double calcZ(Vector p1, Vector p2, Vector p3, double x, double y) {
	double b1u = (p2.x-p1.x)*(p3.z-p1.z)-(p3.x-p1.x)*(p2.z-p1.z);
	double b2u = (p2.y-p1.y)*(p3.z-p1.z)-(p3.y-p1.y)*(p2.z-p1.z);
	
	double ll = (p2.x-p1.x)*(p3.y-p1.y)-(p3.x-p1.x)*(p2.y-p1.y);
	
	return p1.z+(y-p1.y)*b1u/ll-(x-p1.x)*b2u/ll;
}

COLORREF getRGB(double xx, double yy, Vertex *vs) {
	double minZ = -1.0;
	int numVert = -1.0;
	
	for(int n = 0; n < numVerts; n++) {
		if(inVertex(*(vs+n), xx, yy)) {
			double tZ = calcZ((*(vs+n)).v1, (*(vs+n)).v2, (*(vs+n)).v3, xx, yy);
			
			if(minZ == -1.0 || (tZ > 0.1 && tZ < minZ)) {
				minZ = tZ;
				numVert = n;
			}
		}
	}
	if(minZ == -1) {
		return RGB(0, 0, 0);
	}
	return (*(vs+numVert)).col.c;
}

void drawField() {	
	
	Vertex *drawVert = malloc(sizeof(Vertex)*numVerts);
	
	for(int n = 0; n < numVerts; n++) {
		*(drawVert+n) = vertMul(*(verts+n), camera);
		*(drawVert+n) = vertMul(*(drawVert+n), pers);
	}
	for(double i = 0; i < 800.0; i += 1.0) {
		for(double j = 0; j < 600.0; j += 1.0) {
			*(field+(int)j*800+(int)i) = getRGB(i/400-1, j/300-1, drawVert);
		}
	}
}

// Step 4: the Window Procedure
LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch(msg)
    {
        case WM_CLOSE:
            DestroyWindow(hwnd);
        break;
        case WM_DESTROY:
            PostQuitMessage(0); //makes eventhandling loop exit
        break;
		case WM_LBUTTONDOWN:
		{
			
		}
			break;
		case WM_RBUTTONDOWN:
		{
		}
			break;
		case WM_PAINT:
        {
			//MessageBox(0,"PAINT_BEGIN","Kopf",1);
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

			RECT rect;
			short width = 800;
			short height = 600;
			// All painting occurs here, between BeginPaint and EndPaint.
			
			
			// Creating temp bitmap
			HBITMAP map = CreateBitmap(width, 			// width. 512 in my case
									   height, 			// height
									   1, 				// Color Planes, unfortanutelly don't know what is it actually. Let it be 1
									   8*4, 			// Size of memory for one pixel in bits (in win32 4 bytes = 4*8 bits)
									   (void*) field); 	// pointer to array
			// Temp HDC to copy picture
			HDC src = CreateCompatibleDC(hdc); // hdc - Device context for window, I've got earlier with GetDC(hWnd) or GetDC(NULL);
			SelectObject(src, map); // Inserting picture into our temp HDC
			// Copy image from temp HDC to window
			BitBlt(hdc, 		// Destination
				   0,  			// x and
				   0,  			// y - upper-left corner of place, where we'd like to copy
				   width, 		// width of the region
				   height, 		// height
				   src, 		// source
				   0,   		// x and
				   0,   		// y of upper left corner  of part of the source, from where we'd like to copy
				   SRCCOPY); 	// Defined DWORD to juct copy pixels. Watch more on msdn;
			DeleteDC(src); 		// Deleting temp HDC

			//FillRect(hdc, &ps.rcPaint, (HBRUSH) (COLOR_WINDOW+1));

			EndPaint(hwnd, &ps);
		}
		break;
        default:
            return DefWindowProc(hwnd, msg, wParam, lParam);
    }
    return 0;
}


int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    Init3D(6.0/8.0, 100, 0.1, 150);
	gen();
	
	field = malloc(sizeof(COLORREF)*600*800);
	drawField();
    WNDCLASSEX wc; //Window quasi-class. stores params and 'procedure' (control)
    HWND hwnd;
    MSG Msg;

    //Step 1: Registering the Window Class
    wc.cbSize        = sizeof(WNDCLASSEX); //size of struct... why tho?
    wc.style         = 0; //class style (CS_*) probably: https://docs.microsoft.com/en-us/windows/desktop/winmsg/window-class-styles
    wc.lpfnWndProc   = WndProc; //window procedure. i think some sort of event manager
    wc.cbClsExtra    = 0; //extra memory for class
    wc.cbWndExtra    = 0; //extra memory per window
    wc.hInstance     = hInstance; //handle to hinstance (see winMain)
    wc.hIcon         = LoadIcon(NULL, IDI_WARNING); //largeicon (for alt-tab) see https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-loadicona
    wc.hCursor       = LoadCursor(NULL, IDC_ARROW); //see: https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-loadcursora
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW+1); //see: Winuser.h and https://stackoverflow.com/questions/15658341/color-window-in-hbrbackground
    wc.lpszMenuName  = NULL; //soo apparently pointer to string of menu name??
    wc.lpszClassName = g_szClassName; //name of the class
    wc.hIconSm       = LoadIcon(NULL, IDI_WARNING); // small icon

    if(!RegisterClassEx(&wc)) //register class
    {
        MessageBox(NULL, "Window Registration Failed!", "Error!",
            MB_ICONEXCLAMATION | MB_OK);
        return 0;
    }

    // Step 2: Creating the Window
    hwnd = CreateWindowEx(
        0, //sunken inner border around the window... whaa?
        g_szClassName, //class name
        "The title of my window",
        WS_OVERLAPPEDWINDOW, //https://docs.microsoft.com/en-us/windows/desktop/winmsg/window-styles mmmm, shit
        CW_USEDEFAULT, CW_USEDEFAULT, 816, 630, //x,y,w,h
        NULL, NULL, hInstance, NULL);//basically instantiate object from class

    if(hwnd == NULL)
    {
        MessageBox(NULL, "Window Creation Failed!", "Error!",
            MB_ICONEXCLAMATION | MB_OK);
        return 0;
    }

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    // Step 3: The Message Loop
    while(GetMessage(&Msg, NULL, 0, 0) > 0) //event handling implementation (every mouse move too... holy optimisation)
    {
        TranslateMessage(&Msg);
        DispatchMessage(&Msg);
    }
    return Msg.wParam;
}