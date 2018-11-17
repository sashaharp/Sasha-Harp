/******************************************************************************
 *  Compilation:  javac Cosinus.java
 *  Execution:    java Cosinus x
 *  Test:         ./gradlew testen
 *
 *  Eingabe: Ein double Wert x.
 *  Ausgabe: Der Cosinus von x, berechnet mit Hilfe der Taylor Reihe vom Uebungsblatt.
 *
 * 
 ******************************************************************************/

public class Cosinus {
    public static void main(String[] args) {
        if(!(args.length == 1 && Double.parseDouble(args[0]) >= 0)) 
        {
            System.out.println("ERROR");
            return;
        }
        double c = cos(1.0, 1, Double.parseDouble(args[0])%Math.PI)*100;
        System.out.println(((float)(int)c)/100);
    }

    private static double cos(double c, int n, double x) //rekursiv cosinus berechnen
    {
        double cn = pow(-1,n)*pow(x,n*2)/faculty(n*2);
        if(abs(cn*1000.0)<5.0)
            return c + cn;
        else
            return cos(c + cn, n + 1, x);
    }

    private static double abs(double a) //konnte das nicht wirklich rekursiv machen... :(
    {
        if(a < 0)
            return -a;
        return a;
    }

    private static double pow(double a, int b) //rekursiv potenz berechnen (da math.pow nicht erlaubt)
    {
        if (b == 1)
            return a;
        return a * pow(a, b - 1);
    }

    private static int faculty(int n) //rekutsiv fakultaet berechnen 
    {
        if(n == 2)
            return 2;
        return n*faculty(n-1);
    }
}

