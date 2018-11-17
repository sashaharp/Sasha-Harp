/******************************************************************************
 *  Compilation:  javac SimplePrint.java
 *  Execution:    java SimplePrint a b
 *  Test: ./gradlew testen_SimplePrint
 *
 *  Eingabe: Zwei Strings a und b
 *  Ausgabe: Die eingegebenen Strings in umgekehrter Reihenfolge in zwei Zeilen.
 * 
 *  Verwenden Sie fuer alle Ausgaben System.out.print 
 *
 *  Anmerkung: Gehen Sie ausnahmsweise davon aus, dass ihr Programm immer korrekt aufgerufen wird.
 * 
 ******************************************************************************/

public class SimplePrint {
    public static void main(String[] args) {
      System.out.print(args[1] + "\n");
      System.out.print(args[0] + "\n");
    }
}

