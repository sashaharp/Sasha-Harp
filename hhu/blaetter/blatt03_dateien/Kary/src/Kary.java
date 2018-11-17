/******************************************************************************
 *  Compilation:  javac Kary.java
 *  Execution:    java Kary i k
 *  Test:         ./gradlew testen
 *
 *  Eingabe: i ist ein long Wert, k ist ein int Wert zwischen 2 und 16 (jeweils inklusive)
 *  Ausgabe: Die Zahl i (die in der Basis 10 ist) als Zahl zur Basis k. Fuer k > 10 verwenden
 *  Sie die Buchstaben A-F als Ziffern.
 * 
 ******************************************************************************/

public class Kary {
    public static void main(String[] args) {
        if(!(args.length == 2 && Integer.parseInt(args[1]) > 1 && Integer.parseInt(args[1]) < 17))
        {
            System.out.println("ERROR");
            return;
        }
        System.out.println(conv(Integer.parseInt(args[0]), Integer.parseInt(args[1])));
    }

    private static String conv(int n, int b)
    {
        if(n == 0)
            return "";
        return conv((n-(n%b))/b, b) + lookup(n%b);
    }
    
    private static String lookup(int n) //ich mag den hashmap interface nicht...
    {
        int r = 0;
        switch(n)
        {
            case 15: return "F";
            case 14: return "E";
            case 13: return "D";
            case 12: return "C";
            case 11: return "B";
            case 10: return "A";
            case 9: r += 1;
            case 8: r += 1;
            case 7: r += 1;
            case 6: r += 1;
            case 5: r += 1;
            case 4: r += 1;
            case 3: r += 1;
            case 2: r += 1;
            case 1: r += 1;
            case 0: return "" + r;
        }
        return "" + r;
    }
}

