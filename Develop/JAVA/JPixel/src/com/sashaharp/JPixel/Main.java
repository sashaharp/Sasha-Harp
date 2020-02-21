package com.sashaharp.JPixel;

import com.sun.imageio.plugins.png.PNGImageWriter;
import org.lwjgl.*;
import org.lwjgl.glfw.*;
import org.lwjgl.opengl.*;
import org.lwjgl.system.*;
import com.sashaharp.Math2D.*;

import javax.imageio.ImageIO;
import javax.tools.Tool;
import java.awt.image.*;
import java.io.File;
import java.io.IOException;
import java.nio.*;

import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.opengl.GL12.GL_UNSIGNED_INT_8_8_8_8;
import static org.lwjgl.system.MemoryStack.*;
import static org.lwjgl.system.MemoryUtil.*;

public class Main {

    // The window handle
    private long window;

    private Vector3f p00 = new Vector3f(0, 0);
    private Vector3f p01 = new Vector3f(0, 1);
    private Vector3f p11 = new Vector3f(1, 1);
    private Vector3f p10 = new Vector3f(1, 0);
    private Matrix3f transformation = new Matrix3f();
    private int winWidth = 300;
    private int winHeight = 300;
    private boolean control = false;
    private boolean alt = false;
    private boolean shift = false;
    private float mouseX = 0;
    private float mouseY = 0;
    private boolean isInit = true;
    private boolean shutdown = false;

    private int picWidth = 8;
    private int picHeight = 8;
    private int[] texDat = new int[picWidth * picHeight];
    private int tex;
    private String picPath = "";

    public void run() {
        System.out.println("Hello LWJGL " + Version.getVersion() + "!");

        init();
        loop();

        // Free the window callbacks and destroy the window
        glfwFreeCallbacks(window);
        glfwDestroyWindow(window);

        // Terminate GLFW and free the error callback
        glfwTerminate();
        glfwSetErrorCallback(null).free();
    }

    private void init() {
        // Setup an error callback. The default implementation
        // will print the error message in System.err.
        GLFWErrorCallback.createPrint(System.err).set();

        // Initialize GLFW. Most GLFW functions will not work before doing this.
        if ( !glfwInit() )
            throw new IllegalStateException("Unable to initialize GLFW");

        // Configure GLFW
        glfwDefaultWindowHints(); // optional, the current window hints are already the default
        glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE); // the window will stay hidden after creation
        glfwWindowHint(GLFW_RESIZABLE, GLFW_TRUE); // the window will be resizable

        // Create the window
        window = glfwCreateWindow(winWidth, winHeight, "Hello World!", NULL, NULL);
        if ( window == NULL )
            throw new RuntimeException("Failed to create the GLFW window");

        glfwSetFramebufferSizeCallback(window, (window, width, height) -> {
            winWidth = width;
            winHeight = height;
            if(!isInit) {
                glMatrixMode(GL_PROJECTION);
                glLoadIdentity();
                glOrtho(0, winWidth, winHeight, 0, 0, 1);
                glMatrixMode(GL_MODELVIEW);
                glViewport(0, 0, width, height);
            } else
                isInit = false;
        });

        // Setup a key callback. It will be called every time a key is pressed, repeated or released.
        glfwSetKeyCallback(window, (window, key, scancode, action, mods) -> {
            if ( key == GLFW_KEY_ESCAPE && action == GLFW_RELEASE )
                glfwSetWindowShouldClose(window, true); // We will detect this in the rendering loop
            if (key == GLFW_KEY_0)
                Toolbar.getCol(0);
            if (key == GLFW_KEY_1)
                Toolbar.getCol(1);
            if (key == GLFW_KEY_2)
                Toolbar.getCol(2);
            if (key == GLFW_KEY_3)
                Toolbar.getCol(3);
            if (key == GLFW_KEY_4)
                Toolbar.getCol(4);
            if (key == GLFW_KEY_5)
                Toolbar.getCol(5);
            if (key == GLFW_KEY_6)
                Toolbar.getCol(6);
            if (key == GLFW_KEY_7)
                Toolbar.getCol(7);
            if (key == GLFW_KEY_8)
                saveImage();//Toolbar.getCol(8);
            if (key == GLFW_KEY_9)
                loadImage("C:\\Users\\Admin\\Documents\\test.png");//Toolbar.getCol(9);
            if ( key == GLFW_KEY_LEFT_CONTROL || key == GLFW_KEY_RIGHT_CONTROL)
                if (action == GLFW_PRESS)
                    control = true;
                else if (action == GLFW_RELEASE)
                    control = false;
            if ( key == GLFW_KEY_LEFT_ALT || key == GLFW_KEY_RIGHT_ALT)
                if (action == GLFW_PRESS)
                    alt = true;
                else if (action == GLFW_RELEASE)
                    alt = false;
            if ( key == GLFW_KEY_LEFT_SHIFT || key == GLFW_KEY_RIGHT_SHIFT)
                if (action == GLFW_PRESS)
                    shift = true;
                else if (action == GLFW_RELEASE)
                    shift = false;
        });

        glfwSetCursorPosCallback(window, (window, xpos, ypos) -> {
            mouseX = (float)xpos/300;
            mouseY = (float)ypos/300;
        });

        glfwSetMouseButtonCallback(window, (window, button, action, mods) -> {
            if(button == GLFW_MOUSE_BUTTON_LEFT && !alt && !control && !shift) {
                drawAction();
            }else if(button == GLFW_MOUSE_BUTTON_RIGHT && control && alt) {
                transformation = new Matrix3f();
                p00 = new Vector3f(0, 0);
                p01 = new Vector3f(0, 1);
                p11 = new Vector3f(1, 1);
                p10 = new Vector3f(1, 0);
            }
        });

        glfwSetScrollCallback(window, (window, xoffset, yoffset) -> {
            if(Math.abs(yoffset) > 0.5)
                yoffset *= 0.08;
            if(!control && !alt) {
                if(shift)
                    movePic((float)yoffset%1, (float)xoffset%1);
                else
                    movePic((float)xoffset%1, (float)yoffset%1);
            } else if (control) {
                zoomPic((float) yoffset);
            } else if (alt) {
                rotatePic((float)(Math.abs(xoffset)>Math.abs(yoffset) ? xoffset : yoffset)%1);
            }
        });

        // Get the thread stack and push a new frame
        try ( MemoryStack stack = stackPush() ) {
            IntBuffer pWidth = stack.mallocInt(1); // int*
            IntBuffer pHeight = stack.mallocInt(1); // int*

            // Get the window size passed to glfwCreateWindow
            glfwGetWindowSize(window, pWidth, pHeight);

            // Get the resolution of the primary monitor
            GLFWVidMode vidmode = glfwGetVideoMode(glfwGetPrimaryMonitor());

            // Center the window
            glfwSetWindowPos(
                    window,
                    (vidmode.width() - pWidth.get(0)) / 2,
                    (vidmode.height() - pHeight.get(0)) / 2
            );
        } // the stack frame is popped automatically

        // Make the OpenGL context current
        glfwMakeContextCurrent(window);
        // Enable v-sync
        glfwSwapInterval(1);

        // Make the window visible
        glfwShowWindow(window);
    }

    public boolean loadImage(String path) {
        try {
            BufferedImage im = ImageIO.read(new File(path));
            texDat = im.getRGB(0, 0, im.getWidth(), im.getHeight(), null, 0, im.getWidth());
            picPath = path;
            picWidth = im.getWidth();
            picHeight = im.getHeight();
            transformation = Matrix3f.Identity();
            applyTransform();
            glBindTexture(GL_TEXTURE_2D, tex);
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, picWidth, picHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, texDat);
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }

    public boolean saveImage() {
        try {
            DataBuffer rgb = new DataBufferInt(texDat, texDat.length);
            WritableRaster raster = Raster.createPackedRaster(rgb, picWidth, picHeight, picWidth, new int[]{0xff0000, 0xff00, 0xff, 0xff000000}/*r,g,b,a masks*/, null);
            BufferedImage img = new BufferedImage(ColorModel.getRGBdefault(), raster, false, null);
            ImageIO.write(img, "png", new File(picPath));
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }

    private void movePic(float x, float y) {
        transformation.apply(Matrix3f.Translation(x, y));
        applyTransform();
    }

    private void zoomPic(float factor) {
        transformation.apply(Matrix3f.Translation(-mouseX, -mouseY));
        transformation.apply(Matrix3f.Scaling(1f/(1+factor),1f/(1+factor)));
        transformation.apply(Matrix3f.Translation(mouseX, mouseY));
        applyTransform();
    }

    private void rotatePic(float alpha) {
        transformation.apply(Matrix3f.Translation(-0.5f, -0.5f));
        transformation.apply(Matrix3f.Rotation(alpha));
        transformation.apply(Matrix3f.Translation(0.5f, 0.5f));
        applyTransform();
    }

    private void applyTransform() {
        p00 = new Vector3f(0, 0) ;
        p00.apply(transformation);
        p10 = new Vector3f(1, 0) ;
        p10.apply(transformation);
        p11 = new Vector3f(1, 1) ;
        p11.apply(transformation);
        p01 = new Vector3f(0, 1) ;
        p01.apply(transformation);
    }

    private void drawAction() {
        Vector3f mouseVec = new Vector3f(mouseX, mouseY);
        mouseVec.apply(Matrix3f.Inverse(transformation));
        mouseVec.x *= picWidth;
        mouseVec.y *= picHeight;
        if(((int)mouseVec.y)*picWidth + ((int)mouseVec.x) < picWidth * picHeight)
            texDat[((int)mouseVec.y)*picWidth + ((int)mouseVec.x)] = 0xFF000000 | DataSharing.currColor.getRed() | DataSharing.currColor.getGreen()<<8 | DataSharing.currColor.getBlue()<<16;

        glBindTexture(GL_TEXTURE_2D, tex);
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, picWidth, picHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, texDat);
    }

    private void loop() {
        // This line is critical for LWJGL's interoperation with GLFW's
        // OpenGL context, or any context that is managed externally.
        // LWJGL detects the context that is current in the current thread,
        // creates the GLCapabilities instance and makes the OpenGL
        // bindings available for use.
        GL.createCapabilities();

        // Set the clear color
        glClearColor(0.55f, 0.55f, 0.6f, 0.0f);

        for (int i = 0; i < 64; ++i)
            texDat[i] = (byte)(((i + (i / 8)) % 2) * 128 + 127);

        tex = glGenTextures();
        glBindTexture(GL_TEXTURE_2D, tex);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, picWidth, picHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, texDat);

        glMatrixMode(GL_PROJECTION);
        glOrtho(0, 300, 300, 0, 0, 1);
        glMatrixMode(GL_MODELVIEW);

        // Run the rendering loop until the user has attempted to close
        // the window or has pressed the ESCAPE key.
        while ( !glfwWindowShouldClose(window) ) {
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // clear the framebuffer

            glBindTexture(GL_TEXTURE_2D, tex);
            glEnable(GL_TEXTURE_2D);
            glBegin(GL_QUADS);
            glTexCoord2i(0, 0); glVertex2i(Math.round(p00.x * 300), Math.round(p00.y * 300));
            glTexCoord2i(0, 1); glVertex2i(Math.round(p01.x * 300), Math.round(p01.y * 300));
            glTexCoord2i(1, 1); glVertex2i(Math.round(p11.x * 300), Math.round(p11.y * 300));
            glTexCoord2i(1, 0); glVertex2i(Math.round(p10.x * 300), Math.round(p10.y * 300));
            glEnd();
            glDisable(GL_TEXTURE_2D);
            glBindTexture(GL_TEXTURE_2D, 0);

            glfwSwapBuffers(window); // swap the color buffers

            // Poll for window events. The key callback above will only be
            // invoked during this call.
            glfwPollEvents();
        }
        shutdown = true;
    }

    public static void main(String[] args) {
        Runnable r = new Runnable() {
            @Override
            public void run() {
                new Toolbar();
            }
        };
        r.run();
        new Main().run();
    }

}