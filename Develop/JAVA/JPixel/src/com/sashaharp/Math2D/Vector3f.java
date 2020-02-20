package com.sashaharp.Math2D;

public class Vector3f {
    public float x, y = 0;
    public final float z = 1;

    public Vector3f(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public void apply(Matrix3f m) {
        float tx = m.m11 * x + m.m12 * y + m.m13 * z;
        float ty = m.m21 * x + m.m22 * y + m.m23 * z;
        //float tz = m.m31 * x + m.m32 * y + m.m33 * z;
        x = tx;
        y = ty;
        //z = tz;
    }

    public static Vector3f Zero() {
        return new Vector3f(0, 0);
    }
}
