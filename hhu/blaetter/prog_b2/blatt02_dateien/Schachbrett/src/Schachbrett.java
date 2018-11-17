/******************************************************************************
 *  Compilation:  javac Schachbrett.java
 *  Execution:    java Schachbrett n
 *  Test:         ./gradlew testen
 *
 *  Eingabe: Eine positive, ganze Zahl n.
 *  Ausgabe: Ein Schachbrett der Groesse n * n. Schwarze Felder werden durch einen
 *  Stern '*', weisse Felder durch ein Leerzeichen ' ' dargestellt. Das Brett
 *  beginnt mit einem schwarzen Feld.
 *
 * Ueberpruefen Sie, dass die Eingabe positiv ist. Wenn die Eingabe nicht positiv ist,
 * soll das Programm ERROR ausgeben. Andere Fehleingaben koennen Sie ignorieren.
 * 
 ******************************************************************************/

public class Schachbrett {
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        if(N < 0)
        {
            System.out.println("ERROR");
            return;
        }
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < N; j++)
            {
                System.out.print((i+j)%2==0?"*":" ");
            }
            System.out.print("\n");
        }
    }
}

