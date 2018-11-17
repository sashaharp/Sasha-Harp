/******************************************************************************
 *  Compilation:  javac Bughunt01.java
 *  Execution:    java Bughunt01
 *  Test: ./gradlew testen_Bughunt01
 *
 *  Eingabe: Ein double Wert t
 *  Ausgabe: sin(2t)+sin(3t)
 * 
 ******************************************************************************/

public class Bughunt01 {
    public static void main(String[] args) {
        double t = Double.parseDouble(args[0]);
        double result = Math.sin(2*t)+Math.sin(3*t);      
        System.out.println(result);
    }
}
