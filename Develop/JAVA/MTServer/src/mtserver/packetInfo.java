package mtserver;

/**
 * @author sashaharp
 */
public class packetInfo {
    public Boolean get;
    public String key;
    public String[] arguments;
    public String cookie;
    
    public packetInfo(String data) {
        try {
            String[] lines = data.split("\n");
            get = lines[0].split(" ")[0].equals("GET");
            if(!get) {
                String[] msg = lines[0].split(" ")[1].split("_", 3);
                key = msg[1];
                if(key.equals("login")) {
                    arguments = msg[2].split("_", 3);
                } else if(key.equals("admin")) {
                    arguments = msg[2].split("_", 2);
                } else {
                    arguments = new String[] {msg[2]};
                }
            } else {
                key = "";
                arguments = new String[] {lines[0].split(" ")[1]};
            }
            if(data.split("Cookie: ").length > 1) {
                cookie = data.split("Cookie: ")[1].split("\n")[0].trim();
            } else {
                cookie = "";
            }
        } catch(Exception e) {
            get = false;
            key = "";
            arguments = new String[] {};
            cookie = "";
        }
        MTServer.log("New Connection:\r\nget=" + get 
                + "\r\nkey=" + key 
                + "\r\nargs=" + String.join(";", arguments) 
                + "\r\ncookie=" + cookie + "\r\n\r\n");
    }
}
