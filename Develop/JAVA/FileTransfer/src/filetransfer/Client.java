package filetransfer;

import java.io.IOException;
import java.net.Socket;

/**
 * @author sashaharp
 */
public class Client {
    public Socket client;
    private MSG msg;
    private String currentData = "";
    public Client() throws IOException {
        client = new Socket("127.0.0.1", 5002);
        FileTransfer.Log("Created Socket\n\n");
        getFile("/");
    }
    
    public final void getFile(String param) {
        send("GIVE file " + param);
        recv();
        if(msg.code.equals("RECV")) {
            if(msg.cmd.equals("list")) {
                FileTransfer.setListView(msg.data.split("\n"));
            } else if (msg.cmd.equals("data")) {
                int n = Integer.parseInt(msg.params[1]);
                for(int i = 0; i < n; i++) {
                    currentData = "";
                    getFile(param + " " + i);
                }
                FileTransfer.setDataView(currentData);
            } else if(msg.cmd.equals("part")) {
                currentData = currentData+msg.data;
            }
        }
    }
    
    public final void send(String msg) {
        try {
            client.getOutputStream().write(msg.getBytes());
            client.getOutputStream().flush();
            FileTransfer.Log("Successfully sent request:\n"+msg+"\n\n");
        } catch(IOException e) {
            FileTransfer.Log("Error while sending request:\n"+msg+"\n\n");
        }
    }
    public final void recv() {
        byte[] messege_b = new byte[500];
        int n = 0;
        try {
            n = client.getInputStream().read(messege_b, 0, 500);
            FileTransfer.Log("Recieved Messege:\n" + new String(messege_b, 0, n).split("\n")[0] + "\n\n");
        } catch(Exception e) {
            FileTransfer.Log("Failed to revieve a messege\n\n");
        }
        msg = new MSG(new String(messege_b, 0, n));
    }
}
