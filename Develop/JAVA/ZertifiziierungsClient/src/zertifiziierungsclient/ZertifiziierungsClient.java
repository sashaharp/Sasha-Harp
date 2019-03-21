/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zertifiziierungsclient;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.*;

/**
 *
 * @author sashaharp
 */
public class ZertifiziierungsClient {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws IOException {
        Socket client = new Socket("127.0.0.1", 8888);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(client.getOutputStream()));
        bw.write("login-request\n\ntestName\nca071405");
        bw.newLine();
        bw.flush();
        client.close();
    }
}
