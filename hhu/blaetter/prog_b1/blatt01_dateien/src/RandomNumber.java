/******************************************************************************
 *  Compilation:  javac RandomNumber.java
 *  Execution:    java RandomNumber n m
 *  Test: ./gradlew testen_RandomNumber
 *
 *  Eingabe: zwei positive Integer n und m (0 inklusive)
 *  Ausgabe: eine zufällige ganze Zahl zwischen n und m (inklusive der Grenzen)
 *
 *  Anmerkung: Gehen Sie ausnahmsweise davon aus, dass ihr Programm immer korrekt aufgerufen wird.
 * 
******************************************************************************/

public class RandomNumber {
    public static void main(String[] args) {
      int x = Integer.parseInt(args[0]);
      int y = Integer.parseInt(args[1]);
      System.out.println(Math.round(Math.random()*(Math.max(x, y) - Math.min(x, y)) + Math.min(x, y)));
    }
}

