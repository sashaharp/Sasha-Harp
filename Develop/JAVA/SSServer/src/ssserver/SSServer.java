/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ssserver;

import java.io.IOException;

/**
 *
 * @author sashaharp
 */
public class SSServer {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        Ser ver = new Ser();
        ver.run();
    }
    
}
