/******************************************************************************
 *  Compilation:  javac Plateau.java
 *  Execution:    java Plateau x1 x2 x3 ... xn
 *  Test:         ./gradlew testen
 *
 *  Eingabe: Beliebig viele Integer Zahlen.
 *  Ausgabe: Die Laenge und die Startposition des laengsten Plateaus.
 *           Ein Plateau ist eine Sequenz gleicher Zahlen, die durch zwei
 *           niedrigere Zahlen direkt links bzw. rechts davon begrenzt wird.
 *           Die Ausgabe soll ERROR sein, wenn weniger als drei Zahlen
 *           uebergeben werden.
 *           Die Ausgabe fuer die Laenge soll 0 und die Position -1 sein, wenn
 *           es kein laengstes Plateau gibt.
 *           Gehen Sie davon aus, dass es hoechstens ein laengstes Plateau gibt.
 * 
 *  Beispiel:

 $ java Plateau 2 3 3 3 1 2 2 1
 Laenge: 3
 Index: 1

 * In dem Beispiel gibt es zwei Plateaus (Index 1 mit Laenge 3 und Index 5 mit Laenge 2)
 * 
 * 
 ******************************************************************************/

public class Plateau {
    public static void main (String args[]){
        int len = 0;
        int ind = -1;
        if(args.length < 3)
        {
            System.out.println("ERROR");
            return;
        }
        for(int i = 1; i < args.length - 1; i++)
        {
            if(Integer.parseInt(args[i-1]) < Integer.parseInt(args[i]))
            {
                int tind = i;
                int tlen = 0;
                while(i < args.length - 2 && Integer.parseInt(args[i+1]) == Integer.parseInt(args[i]))
                {
                    i++;
                    tlen++;
                }
                if(Integer.parseInt(args[i+1]) < Integer.parseInt(args[i]) && tlen >= len)
                {
                    len = tlen+1;
                    ind = tind;
                }
            }
        }
        System.out.println("Laenge: " + len);
        System.out.println("Index: " + ind);
    }
}

