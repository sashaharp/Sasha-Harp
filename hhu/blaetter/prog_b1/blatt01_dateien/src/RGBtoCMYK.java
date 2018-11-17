/******************************************************************************
 *  Compilation:  javac RGBtoCMYK.java
 *  Execution:    java RGBtoCMYK r g b
 *  Test: ./gradlew testen_RGBtoCMYK
 *
 *  Eingabe: Drei ganze Zahlen zwischen 0 und 255, die eine RGB Farbe bezeichnen
 *
 *  Ausgabe: Die Farbe im CMYK Farbschema. Ausgabecodierung (C,M,Y,K)
 *
 *  Die Formeln zur Berechnung finden Sie auf dem Aufgabenblatt und im Buch (Aufgabe 1.2.32)
 *
 *  Anmerkungen:
 *    Gehen Sie ausnahmsweise davon aus, dass ihr Programm immer korrekt aufgerufen wird.
 *
 *  Referenzen:
 *    http://docs.oracle.com/javase/8/docs/api/java/lang/Math.html
 *    https://de.wikipedia.org/wiki/RGB-Farbraum
 *    https://de.wikipedia.org/wiki/CMYK-Farbmodell

 * 
 ******************************************************************************/

public class RGBtoCMYK {
    public static void main(String[] args) {
        short r = Short.parseShort(args[0]);
        short g = Short.parseShort(args[1]);
        short b = Short.parseShort(args[2]);
        float w = ((float)Math.max(Math.max(r, g), b))/255.0f;
        float c = (w - ((float)r)/255)/w;
        float m = (w - ((float)g)/255)/w;
        float y = (w - ((float)b)/255)/w;
        float k = 1-w;
        System.out.println("(" + c + "," + m + "," + y + "," + k + ")");
    }
}

