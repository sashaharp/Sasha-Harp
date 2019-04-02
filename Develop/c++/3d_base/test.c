#include "3dRender.h"
#include <gtk/gtk.h>
#include <stdio.h>

#define ROWS 600
#define COLS 600
#define BYTES_PER_PIXEL 3

char inside(Vertex t, Vector v) {
    double A1 = 
}

void bw_to_rgb(guchar *rgb, guchar *bw, size_t sz) {
    for (size_t i = 0; i < sz; i++)
        for (size_t j = 0; j < BYTES_PER_PIXEL; j++)
            rgb[i * BYTES_PER_PIXEL + j] = bw[i];
}

void gen() {
    Vector points[8];
    points[0] = vect(-1, -1, 5);
    points[1] = vect(-1,  1, 5);
    points[2] = vect( 1,  1, 5);
    points[3] = vect( 1, -1, 5);
    points[4] = vect(-1, -1, 7);
    points[5] = vect(-1,  1, 7);
    points[6] = vect( 1,  1, 7);
    points[7] = vect( 1, -1, 7);

    Vertex verts[12];
    verts[0] = vert(points[0], points[1], points[2]);
    verts[1] = vert(points[0], points[2], points[3]);
    
    verts[2] = vert(points[4], points[5], points[6]);
    verts[3] = vert(points[4], points[6], points[7]);
    
    verts[4] = vert(points[0], points[1], points[5]);
    verts[5] = vert(points[0], points[5], points[4]);
    
    verts[6] = vert(points[3], points[2], points[6]);
    verts[7] = vert(points[3], points[6], points[7]);
    
    verts[8] = vert(points[1], points[2], points[6]);
    verts[9] = vert(points[1], points[6], points[5]);
    
    verts[10] = vert(points[0], points[1], points[7]);
    verts[11] = vert(points[0], points[7], points[4]);
    
    Object *o = obj_init(verts, translate(0, 0, 0), 12);
    printf("(%f | %f | %f)\n",(*(*o).triangles).v1.x, (*(*o).triangles).v1.y, (*(*o).triangles).v1.z);
}

int main(int argc, char **argv) {

    guchar rgb[ROWS * COLS * BYTES_PER_PIXEL];
    
    Init3D(1, 100, 0.1, 100);
    gen();

    for(int n = 0; n < ROWS * COLS; n++) {
        rgb[n*3] = n*255/(ROWS*COLS);
        rgb[n*3+1] = n*255/(ROWS*COLS);
        rgb[n*3+2] = n*255/(ROWS*COLS);
    }

    gtk_init(&argc, &argv);

    GdkPixbuf *pb = gdk_pixbuf_new_from_data(
        rgb,
        GDK_COLORSPACE_RGB,     // colorspace (must be RGB)
        0,                      // has_alpha (0 for no alpha)
        8,                      // bits-per-sample (must be 8)
        COLS, ROWS,             // cols, rows
        COLS * BYTES_PER_PIXEL, // rowstride
        NULL, NULL              // destroy_fn, destroy_fn_data
    );
    GtkWidget *image = gtk_image_new_from_pixbuf(pb);

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Image");
    gtk_window_set_default_size(GTK_WINDOW(window), COLS+20, ROWS+20);
    gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);
    gtk_container_add(GTK_CONTAINER(window), image);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);
    gtk_widget_show_all(window);

    gtk_main();

    return 0;
}