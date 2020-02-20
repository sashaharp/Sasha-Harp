package com.sashaharp.Math2D;

public class Matrix3f {
    public float m11,m12,m13,m21,m22,m23,m31,m32,m33 = 0f;
    public Matrix3f() {
        m11 = 1;
        m22 = 1;
        m33 = 1;
    }

    public void apply(Matrix3f m) {
        float tm11 = m11 * m.m11 + m21 * m.m12 + m31 * m.m13;
        float tm12 = m12 * m.m11 + m22 * m.m12 + m32 * m.m13;
        float tm13 = m13 * m.m11 + m23 * m.m12 + m33 * m.m13;

        float tm21 = m11 * m.m21 + m21 * m.m22 + m31 * m.m23;
        float tm22 = m12 * m.m21 + m22 * m.m22 + m32 * m.m23;
        float tm23 = m13 * m.m21 + m23 * m.m22 + m33 * m.m23;

        float tm31 = m11 * m.m31 + m21 * m.m32 + m31 * m.m33;
        float tm32 = m12 * m.m31 + m22 * m.m32 + m32 * m.m33;
        float tm33 = m13 * m.m31 + m23 * m.m32 + m33 * m.m33;

        m11 = tm11;m12 = tm12;m13 = tm13;
        m21 = tm21;m22 = tm22;m23 = tm23;
        m31 = tm31;m32 = tm32;m33 = tm33;
    }

    public static Matrix3f Identity() {
        return new Matrix3f();
    }

    public static Matrix3f Translation(float x, float y) {
        Matrix3f m = new Matrix3f();
        m.m13 = x;
        m.m23 = y;
        return m;
    }

    public static Matrix3f Rotation(float alpha) {
        Matrix3f m = new Matrix3f();
        m.m11 = (float)Math.cos(alpha);
        m.m12 = (float)Math.sin(alpha) * -1;
        m.m21 = -1 * m.m12;
        m.m22 = m.m11;
        return m;
    }

    public static Matrix3f Scaling(float x, float y) {
        Matrix3f m = new Matrix3f();
        m.m11 = x;
        m.m22 = y;
        return m;
    }

    public static Matrix3f Inverse(Matrix3f m) {
        Matrix3f inv = new Matrix3f();
        inv.m11 = m.m22*m.m33-m.m23*m.m32;
        inv.m12 = m.m13*m.m32-m.m12*m.m33;
        inv.m13 = m.m12*m.m23-m.m13*m.m22;
        inv.m21 = m.m23*m.m31-m.m21*m.m33;
        inv.m22 = m.m11*m.m33-m.m13*m.m31;
        inv.m23 = m.m13*m.m21-m.m11*m.m23;
        inv.m31 = m.m21*m.m32-m.m22*m.m31;
        inv.m32 = m.m12*m.m31-m.m11*m.m32;
        inv.m33 = m.m11+m.m22-m.m12*m.m21;
        float det = m.m11 * inv.m11 + m.m12 * inv.m21 + m.m13 * inv.m31;
        if(det == 0)
            return null;
        inv.m11 /= det;
        inv.m12 /= det;
        inv.m13 /= det;
        inv.m21 /= det;
        inv.m22 /= det;
        inv.m23 /= det;
        inv.m31 /= det;
        inv.m32 /= det;
        inv.m33 /= det;
        return inv;
    }
}
