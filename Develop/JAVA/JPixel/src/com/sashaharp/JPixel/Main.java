package com.sashaharp.JPixel;

import org.lwjgl.*;
import org.lwjgl.glfw.*;
import org.lwjgl.opengl.*;
import org.lwjgl.system.*;

import java.nio.*;

import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.system.MemoryStack.*;
import static org.lwjgl.system.MemoryUtil.*;

public class Main {

    static class Vec2 {
        float x;
        float y;
        public Vec2(float x, float y) {
            this.x = x;
            this.y = y;
        }
        public void rotate(float alpha) {
            float tx = x * (float)Math.cos(alpha) - y * (float)Math.sin(alpha);
            float ty = x * (float)Math.sin(alpha) + y * (float)Math.cos(alpha);
            x = tx;
            y = ty;
        }
        public void stretch(float factor) {
            x *= factor;
            y *= factor;
        }
        public void translate(float xoffset, float yoffset) {
            x += xoffset;
            y += yoffset;
        }
    }

    // The window handle
    private long window;

    private Vec2 p00 = new Vec2(0, 0);
    private Vec2 p01 = new Vec2(0, 1);
    private Vec2 p11 = new Vec2(1, 1);
    private Vec2 p10 = new Vec2(1, 0);
    private int winWidth = 300;
    private int winHeight = 300;
    private boolean control = false;
    private boolean alt = false;
    private boolean shift = false;
    private float mouseX = 0;
    private float mouseY = 0;
    private boolean isInit = true;
    private boolean shutdown = false;

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

        });

        glfwSetScrollCallback(window, (window, xoffset, yoffset) -> {
            if(!control && !alt) {
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

    private void movePic(float x, float y) {
        p00.translate(x, y);
        p01.translate(x, y);
        p11.translate(x, y);
        p10.translate(x, y);
    }

    private void zoomPic(float factor) {
        p00.translate(-mouseX, -mouseY);
        p00.stretch(1/(1+factor));
        p00.translate(mouseX, mouseY);
        p01.translate(-mouseX, -mouseY);
        p01.stretch(1/(1+factor));
        p01.translate(mouseX, mouseY);
        p11.translate(-mouseX, -mouseY);
        p11.stretch(1/(1+factor));
        p11.translate(mouseX, mouseY);
        p10.translate(-mouseX, -mouseY);
        p10.stretch(1/(1+factor));
        p10.translate(mouseX, mouseY);
    }

    private void rotatePic(float alpha) {
        p00.translate(-0.5f, -0.5f);
        p00.rotate(alpha);
        p00.translate(0.5f, 0.5f);
        p01.translate(-0.5f, -0.5f);
        p01.rotate(alpha);
        p01.translate(0.5f, 0.5f);
        p11.translate(-0.5f, -0.5f);
        p11.rotate(alpha);
        p11.translate(0.5f, 0.5f);
        p10.translate(-0.5f, -0.5f);
        p10.rotate(alpha);
        p10.translate(0.5f, 0.5f);
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

        short[] texDat = new short[64];
        for (int i = 0; i < 64; ++i)
            texDat[i] = (byte)(((i + (i / 8)) % 2) * 128 + 127);

        int tex = glGenTextures();
        glBindTexture(GL_TEXTURE_2D, tex);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
        glTexImage2D(GL_TEXTURE_2D, 0, GL_LUMINANCE, 8, 8, 0, GL_LUMINANCE, GL_UNSIGNED_SHORT, texDat);

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