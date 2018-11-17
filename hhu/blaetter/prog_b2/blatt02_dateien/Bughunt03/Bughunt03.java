/******************************************************************************
 *  Compilation:  javac Bughunt03.java
 *  Execution:    java Bughunt03 n
 *
 *  Eingabe: 1 oder 2  
 *  Ausgabe: für die Aufgabe nicht relevant 
 *
 ******************************************************************************/

public class Bughunt03 {
    public static void main(String[] args) {

        int mode = Integer.parseInt(args[0]);
        if (mode == 1) {  
            for(double d=0; d != 1.0; d = d + 0.1) { 
                System.out.println(d);
            }     
            System.out.println(mode);
        }

        if (mode == 2) {
            double x = 9007199254740900.0;  
            for(double i=x; i < x + 100.0 ; i++) { 
                System.out.print(i); 
            }  
            System.out.println();
            System.out.println(mode);
        }

    }
}
