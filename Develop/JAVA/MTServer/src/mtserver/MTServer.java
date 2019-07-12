package mtserver;

import java.io.File;
import java.io.IOException;
import java.lang.Thread.State;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

/**
 *
 * @author sashaharp
 */
public class MTServer {

    public static String SERVERPATH;
    
    public static void main(String[] args) throws InterruptedException, IOException{
        Database lock = new Database();
        ServerThread s1 = new ServerThread("s1", lock);
        ServerThread s2 = new ServerThread("s2", lock);
        ServerThread s3 = new ServerThread("s3", lock);
        ServerThread s4 = new ServerThread("s4", lock);
        
        while(true) {
            Thread.sleep(1000 * 30);
            if(lock.server.isClosed())
                lock.server = new ServerSocket(5001, 150, InetAddress.getLocalHost());
            if(s1.state == -1)
                s1 = new ServerThread("s1", lock);
            if(s2.state == -1)
                s2 = new ServerThread("s2", lock);
            if(s3.state == -1)
                s3 = new ServerThread("s3", lock);
            if(s4.state == -1)
                s4 = new ServerThread("s4", lock);
        }
    }
    
    public static void log(String msg) {
        System.out.println(msg);
        File f = new File(SERVERPATH + "/log.temp");
        try {
            if(!f.exists()) {
                f.createNewFile();
            }
            Files.write(f.toPath(), msg.getBytes(), StandardOpenOption.APPEND);
        } catch(Exception e) {}
    }
    
}
