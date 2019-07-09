package mtserver;

import java.util.ArrayList;
import java.util.List;

/**
 * @author sashaharp
 */
public class MAData {
    public String Y_Kennung;
    public int page;
    public String currentSS;
    public List<Boolean> answs;
    public int tries;
    
    public MAData(String Y_Kennung, int page, String currentSS) {
        this.Y_Kennung = Y_Kennung;
        this.page = page;
        this.currentSS = currentSS;
        this.answs = new ArrayList<Boolean>();
        this.tries = 0;
    }
}
