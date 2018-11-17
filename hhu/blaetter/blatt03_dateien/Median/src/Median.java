/******************************************************************************
 *  Compilation:  javac Median.java
 *  Execution:    java Median a b c d e
 *  Testen:       ./gradlew testen
 *
 *  Eingabe: Fuenf unterschiedliche ganze Zahlen a, b, c, d und e.
 *  Ausgabe: Der Median der Werte, d.h. eine der fuenf Zahlen, so dass genau
 *           zwei der Zahlen kleiner und zwei der Zahlen groesser sind.
 *
 *  Referenzen: https://de.wikipedia.org/wiki/Euklidischer_Algorithmus#Iterative_Variante
 * 
 ******************************************************************************/

public class Median {
    private static int a;
    private static int b;
    private static int c;
    private static int d;
    private static int e;

    public static void main(String[] args) {
        if(args.length != 5)
        {
            System.out.println("ERROR");
            return;
        }
        a = Integer.parseInt(args[0]); 
        b = Integer.parseInt(args[1]);
        c = Integer.parseInt(args[2]);
        d = Integer.parseInt(args[3]);
        e = Integer.parseInt(args[4]);
        if(countBigger(a))
            System.out.println(a);
        else if(countBigger(b))
            System.out.println(b);
        else if(countBigger(c))
            System.out.println(c);
        else if(countBigger(d))
            System.out.println(d);
        else if(countBigger(e))
            System.out.println(e);
    }

    private static Boolean countBigger(int t)
    {
        int cnt = 0;
        if (t > a)
            cnt++;
        if (t > b)
            cnt++;
        if (t > c)
            cnt++;
        if (t > d)
            cnt++;
        if (t > e)
            cnt++;
        return cnt==2;
    }
}

