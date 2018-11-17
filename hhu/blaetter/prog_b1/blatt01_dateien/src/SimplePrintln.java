/******************************************************************************
 *  Compilation:  javac SimplePrintln.java
 *  Execution:    java SimplePrintln a b
 *  Test: ./gradlew testen_SimplePrintln
 *
 *  Eingabe: Zwei Strings a und b
 *  Ausgabe: Die eingegebenen Strings in umgekehrter Reihenfolge in zwei Zeilen.
 * 
 *  Verwenden Sie fuer alle Ausgaben System.out.println 
 *
 *  Anmerkung: Gehen Sie ausnahmsweise davon aus, dass ihr Programm immer korrekt aufgerufen wird.
 * 
 ******************************************************************************/

public class SimplePrintln {
    public static void main(String[] args) {
      System.out.println(args[1]);
      System.out.println(args[0]);
    }
}

