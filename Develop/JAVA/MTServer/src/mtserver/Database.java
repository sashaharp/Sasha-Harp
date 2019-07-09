package mtserver;

import java.io.IOException;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.UnknownHostException;
import java.util.List;

/**
 * @author sashaharp
 */
public class Database {
    public List<MAData> entries;
    public ServerSocket server;
    public String admin;
    
    public Database() throws UnknownHostException, IOException {
        server = new ServerSocket(5001, 150, InetAddress.getLocalHost());
    }
    
    public int contains(String Y) {
        for(int n = 0; n < entries.size(); n++) {
            if(entries.get(n).Y_Kennung.equals(Y)) {
                return n;
            }
        }
        return -1;
    }
    
    public Boolean add(String Y, int page, String currentSS) {
        int n;
        if((n = this.contains(Y)) > -1) {
            this.entries.get(n).page = page;
            this.entries.get(n).currentSS = currentSS;
            return true;
        }
        this.entries.add(new MAData(Y, page, currentSS));
        return false;
    }
    
    public Boolean turnPage() {
        return true;
    }
}
