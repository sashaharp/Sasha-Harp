package filetransfer;

/**
 * @author sashaharp
 */
public class MSG {
    public String code;
    public String cmd;
    public String[] params;
    public String data;
    public MSG(String msg) {
        if(msg.split("\n")[0].split(" ").length > 2) {
            code = msg.split("\n")[0].split(" ")[0];
            cmd = msg.split("\n")[0].split(" ")[1];
            params = msg.split("\n")[0].split(" ", 3)[2].split(" ");
            if(msg.split("\n").length > 1) {
                data = msg.split("\n", 2)[1];
            }
        } else {
            code = "";
            cmd = "";
            params = new String[]{};
            data = "";
        }
    }
}
