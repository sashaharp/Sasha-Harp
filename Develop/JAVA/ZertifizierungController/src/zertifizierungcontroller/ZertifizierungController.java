package zertifizierungcontroller;

import java.io.IOException;

public class ZertifizierungController {
    public static void main(String[] args) throws IOException, Exception {
        Ser ver = new Ser(12);
        
        ver.start();
        mainWindow.main();
    }
    
    
    
}

