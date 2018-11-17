/******************************************************************************
 *  Compilation:  javac Bughunt02.java
 *  Execution:    java Bughunt02 a1 a2 a3 b1 b2 b3
 *  Test:         ./gradlew testen
 *
 *  Eingabe: Die Komponenten von zwei Vektoren a und b. 
 *  Ausgabe: Das Kreuzprodukt der beiden Vektoren.
 *
 *  Referenzen: https://de.wikipedia.org/wiki/Kreuzprodukt
 *
 * 
 ******************************************************************************/

public class Bughunt02 {
    public static void main(String[] args) {
        if (args.length != 6) {
            System.out.println("ERROR");
        }
        else {
      	    double a1 = Double.parseDouble(args[0]);
      	    double a2 = Double.parseDouble(args[1]);
      	    double a3 = Double.parseDouble(args[2]);
      	    double b1 = Double.parseDouble(args[3]);
      	    double b2 = Double.parseDouble(args[4]);
      	    double b3 = Double.parseDouble(args[5]);
      
      	    // Berechnung entsprechend der Definition in der Wikipedia

      	    double c1 = a2*b3-a3*b2;
      	    double c2 = a3*b1-a1*b3;
      	    double c3 = a1*b2-a2*b1;
      	    System.out.println(c1 + " " + c2 + " " + c3);
    	}
    }
}

