/******************************************************************************
 *  Compilation:  javac Gcd.java
 *  Execution:    java Gcd a b
 *  Test:         ./gradlew testen
 *
 *  Eingabe: Zwei nicht-negative, ganze Zahlen a und b.
 *  Ausgabe: Der groesste gemeinsame Teiler. Benutzen Sie den Euklidischen Algorithmus zur Berechnung.
 *
 *  Referenzen: https://de.wikipedia.org/wiki/Euklidischer_Algorithmus#Iterative_Variante
 *
 * Ueberpruefen Sie, dass die Eingaben nicht-negativ sind. Wenn mindestens eine Eingabe negativ ist,
 * soll das Programm ERROR ausgeben. Andere Fehleingaben koennen Sie ignorieren.
 * 
 ******************************************************************************/

public class Gcd {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        if(a<0||b<0){System.out.println("ERROR");return;}
        while(b != 0)
        {
            int t = a%b;
            a = b;
            b = t;
        }
        System.out.println(a);
    }
}

