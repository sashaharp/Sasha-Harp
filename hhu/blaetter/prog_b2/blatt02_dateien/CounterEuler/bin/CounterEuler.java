/******************************************************************************
 *  Compilation:  javac CounterEuler.java
 *  Execution:    java CounterEuler
 *  Test:         ./gradlew testen
 *
 *  Eingabe: -
 *  Ausgabe: positive, ganze Zahlen a,b,c,d,e, die die Eulersche Vermutung widerlegen.
 *
 *  Verwenden Sie fuenf ineinandergeschachtelte Schleifen um die Loesung zu finden. 
 *  Es genuegt nicht, den Testfall zu erfuellen indem Sie das Ergebnis ausgeben. 
 *
 *  Sie koennen als Obergrenze fuer alle Werte 200 verwenden.
 *
 *  Tipps:
 *  1) Sie koennen die Suche nach Loesungen dramatisch beschleunigen, indem
 *  Sie die Tatsache verwenden, dass die Loesungen symmetrisch sind. Angenommen
 *  Sie pruefen gerade Loesungen mit a = 15. Dann brauchen Sie fuer b keine Werte
 *  zu pruefen, die kleiner sind als 15. Gaebe es eine Loesung, haetten Sie diese
 *  bereits gefunden.
 *  2) Wenn Sie eine Loesung gefunden haben, koennen Sie aufhoeren zu suchen.
 *
 *  Bei Verwendung dieser Tipps findet man die Loesung in wenigen Sekunden, ohne
 *  Tipp 1 benoetigt man einige Minuten.
 *
 * 
 ******************************************************************************/

public class CounterEuler {
    public static void main(String[] args) {
        for(int i = 1; i < 200; i++)
        {
            for(int j = i; j < 200; j++)
            {
                for(int k = j; k < 200; k++)
                {
                    for(int l = k; l < 200; l++)
                    {
                        for(int m = Math.max(Math.max(Math.max(i, j), k), l); m < 200; m++) //i^5+j^5+k^5+l^5=m^5 => m^5 > i, j, k, l
                        {
                            if((Math.pow(i, 5)+Math.pow(j, 5)+Math.pow(k, 5)+Math.pow(l, 5))==Math.pow(m, 5))
                            {
                                System.out.println("" + i + "," + j + "," + k + "," + l + "," + m);
                                return;
                            }
                        }
                    }
                }
            }
        } 
    }
}

