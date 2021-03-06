package ssserver;


import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * @author sashaharp
 */
public class Ser extends Thread {
    private static ServerSocket server;
    public boolean Running;
    public static Ser ver;
    int PORT_NO;
    static String SERVERPATH = "O:/040 Kundencenter/055 Management/2_Themen/12_Performance_Management/2_Themen/Entwicklung/JSocks/";//"/home/sashaharp/Documents/git/Sasha-Harp/Develop/JAVA/SSServer/pFolder/";//
    HashMap<String, Integer> Ys = new HashMap<String, Integer>();
    HashMap<String, String> SSnums = new HashMap<String, String>();
    HashMap<String, List<Boolean>> answs = new HashMap<String, List<Boolean>>();
    HashMap<String, Integer> tries = new HashMap<String, Integer>();
    
    String admin = "123!@#456$%^789&*(";
    
    public static void log(String s) throws IOException {
        File f = new File(SERVERPATH + "/log.temp");
        if(!f.exists()) {
            f.createNewFile();
            Files.write(f.toPath(), "HTTP/1.1 200 OK\r\nServer: Apache/1.3.29 (Unix) PHP/4.3.4\r\nContent-Length: 64000\r\nContent-Language: en_US\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n".getBytes());
        }
        Files.write(f.toPath(), (new SimpleDateFormat("MM.dd HH:mm:ss").format(Calendar.getInstance().getTime()) + "$ " + s + "<br><br>").getBytes(), StandardOpenOption.APPEND);
        System.out.println(new SimpleDateFormat("MM.dd HH:mm:ss").format(Calendar.getInstance().getTime()) + "$ " + s + "\n");
    }
    
    public void crash() throws IOException {
        File f = new File(SERVERPATH + "/crash.state");
        if(f.exists()) {
            f.delete();
        }
        f.createNewFile();
        String so = "";
        for(String k : Ys.keySet()) {
            so = so + k + ":" + Ys.get(k) + ";";
        }
        if(so.length()==0) 
            return;
        so = so.substring(0, so.length()-1) + "\n";
        for(String k : SSnums.keySet()) {
            so = so + k + ":" + SSnums.get(k) + ";";
        }
        so = so.substring(0, so.length()-1) + "\n";
        for(String k : answs.keySet()) {
            so = so + k + ":";
            for(Boolean b : answs.get(k)) {
                so = so + b + ":";
            }
            so = so.substring(0, so.length()-1) + ";";
        }
        so = so.substring(0, so.length()-1) + "\n";
        for(String k : tries.keySet()) {
            so = so + k + ":" + tries.get(k) + ";";
        }
        so = so.substring(0, so.length()-1);
        if(so.length() < 4) {
            so = "\n\n\n\n";
        }
        Files.write(f.toPath(), so.getBytes());
    }
    
    Ser() throws IOException {
        this.PORT_NO = 5001;
        ver = this;
        this.Running = true;
        File f = new File(SERVERPATH + "/crash.state");
        try {
            if(f.exists()) {
                List<String> ls = Files.readAllLines(f.toPath());
                if(ls.size()>0 && ls.get(0).length()>0) {
                    for(String v : ls.get(0).split(";")) {
                        Ys.putIfAbsent(v.split(":")[0], Integer.parseInt(v.split(":")[1]));
                    }
                    for(String v : ls.get(1).split(";")) {
                        SSnums.putIfAbsent(v.split(":")[0], v.split(":")[1]);
                    }
                    for(String v : ls.get(2).split(";")) {
                        List<Boolean> temp = new ArrayList<Boolean>();
                        for(int n = 1; n < v.split(":").length; n++) {
                            temp.add(Boolean.parseBoolean(v.split(":")[n]));
                        }
                        answs.putIfAbsent(v.split(":")[0], temp);
                    }
                    for(String v : ls.get(3).split(";")) {
                        tries.putIfAbsent(v.split(":")[0], Integer.parseInt(v.split(":")[1]));
                    }
                }
                f.delete();
            }
        } catch(Exception ex) { }
    }
    
    @Override
    public void run() {
        try {
            server = new ServerSocket(PORT_NO, 150, InetAddress.getLocalHost());//getLoopbackAddress()
            log("Server Launch");
            listen();
        } catch (Exception ex) {
            try {
                log(ex.getMessage());
            } catch (IOException ex1) {
                Logger.getLogger(Ser.class.getName()).log(Level.SEVERE, null, ex1);
            }
            Logger.getLogger(Ser.class.getName()).log(Level.SEVERE, null, ex);
        }
        try {
            crash();
        } catch (IOException ex) {
            Logger.getLogger(Ser.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    private void listen() throws Exception {
        boolean b = true;
        while(b) {
            String data = null;
            Socket client = server.accept();
            String clientAddress = client.getInetAddress().getHostAddress();
            log("\r\nNew connection from " + clientAddress);

            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            char[] buffer = new char[1000];
            in.read(buffer);
            String dataRecieved = String.valueOf(buffer);
            log("recieved: " + dataRecieved);
            
            if(dataRecieved.length() > 20 && dataRecieved.split(" ").length > 1) {
                String coockie = "";
                try {
                    coockie = dataRecieved.split("Cookie: ")[1].split("\n")[0].trim();
                } catch (Exception ex) {
                    try {
                        log(ex.getMessage());
                    } catch (IOException ex1) {
                        Logger.getLogger(Ser.class.getName()).log(Level.SEVERE, null, ex1);
                    }
                }
                if("/key".equals(dataRecieved.split("\n")[0].split(" ")[1].split("_", -1)[0])) {
                    String[] keys = dataRecieved.split("\n")[0].split(" ")[1].split("_", -1);
                    log("Key : " + keys[1]);
                    if("login".equals(keys[1])) {
                        String[] MAs = Files.readAllLines(Paths.get(SERVERPATH + "MAs.txt"), StandardCharsets.ISO_8859_1).get(0).split(",", -1);
                        String[] pswds = Files.readAllLines(Paths.get(SERVERPATH + "MAs.txt"), StandardCharsets.ISO_8859_1).get(3).split(",", -1);
                        if(Arrays.asList(MAs).contains(keys[2]) && (pswds.length <= Arrays.asList(MAs).indexOf(keys[2]) || pswds[Arrays.asList(MAs).indexOf(keys[2])].equals(keys[3]))) {
                            Ys.put(keys[2].trim(), 1);
                            tries.put(keys[2].trim(), 0);
                            log("Added: " + keys[2].trim());
                        } else {
                            log(keys[2].trim() + " not found!");
                        }
                    } else if("admin".equals(keys[1])) {
                        if("d534ba14".equals(keys[2].trim())) {
                            admin = coockie;
                            Ys.put(admin, 0);
                            SSnums.put(admin, dataRecieved.split("\n")[0].split(" ")[1].split("_", 4)[3]);
                        }
                    } else if(Ys.containsKey(coockie) && "result".equals(keys[1])) {
                        answs.putIfAbsent(coockie, new ArrayList<Boolean>());
                        for(String ans: keys[2].split("-", -1)){
                            answs.get(coockie).add("true".equals(ans)); //not sure!!
                        }
                    } else if(Ys.containsKey(coockie) && "SSnum".equals(keys[1])) {
                        SSnums.put(coockie, dataRecieved.split("\n")[0].split(" ")[1].split("_", 3)[2]);
                    } else if("kia".equals(keys[1])) {
                        Ys.remove(coockie);
                        log("Removed id: " + coockie);
                        if(answs.containsKey(coockie)) {
                            File f = new File(SERVERPATH + SSnums.get(coockie) + "/Results/" + coockie);
                            if(!f.exists()) {
                                f.createNewFile();
                            }
                            String tempRes = "";
                            for(int k = 0; k < Math.min(Files.readAllLines(Paths.get(SERVERPATH + SSnums.get(coockie) + "/result.txt"), StandardCharsets.ISO_8859_1).get(0).split(";", -1).length, answs.get(coockie).size()); k++){
                                tempRes += (answs.get(coockie).get(k)?"true":"false") + ";";
                            }
                            Files.write(f.toPath(), ("result:\r\n" + tempRes.substring(0, tempRes.length()-1) + "\r\n").getBytes(), StandardOpenOption.APPEND);
                            answs.remove(coockie);
                        }
                        SSnums.remove(coockie);
                        admin = "123!@#456$%^789&*(";
                    } else if(Ys.containsKey(coockie) && "next".equals(keys[1])) {
                        log("next page loaded, coockie = " + coockie + ", value = " + Ys.get(coockie));
                        if(Ys.get(coockie) > 0) {
                            Ys.put(coockie, Ys.get(coockie)+1);
                        } else {
                            log("next test loaded");
                            Ys.put(coockie, Ys.get(coockie)-1);
                        }
                    } else if(Ys.containsKey(coockie) && "prev".equals(keys[1])) {
                        if(Ys.get(coockie) > 1) {
                            Ys.put(coockie, Ys.get(coockie)-1);
                        } else if(Ys.get(coockie) == 0) {
                            int n = 1;
                            while((new File(SERVERPATH + SSnums.get(coockie) + "/Folien/Folie" + (n+1) + ".PNG")).exists()) {
                                n++;
                            }
                            Ys.put(coockie, n);
                        } else if(Ys.get(coockie) < 0) {
                            if(tries.get(coockie) != 3) {
                                Ys.put(coockie, -1);
                                answs.put(coockie, new ArrayList<Boolean>());
                                tries.put(coockie, tries.get(coockie)+1);
                            }
                        }
                    }
                } else if(Ys.containsKey(coockie) && "/Foli".equals(dataRecieved.split("\n")[0].split(" ")[1].split("e")[0])) {
                    log("Coockie: " + coockie);
                    byte[] y = new byte[]{};
                    if(Ys.get(coockie) > 0) {
                        log("searching for: " + SERVERPATH + SSnums.get(coockie) + "/Folien/Folie" + Ys.get(coockie) + ".PNG");
                        log("" + (new File(SERVERPATH + SSnums.get(coockie) + "/Folien/Folie" + Ys.get(coockie) + ".PNG")).exists());
                        if((new File(SERVERPATH + SSnums.get(coockie) + "/Folien/Folie" + Ys.get(coockie) + ".PNG")).exists()) {
                            y = Files.readAllBytes(Paths.get(SERVERPATH + SSnums.get(coockie) + "/Folien/Folie" + Ys.get(coockie) + ".PNG"));
                        } else {
                            Ys.put(coockie, 0);
                            y = Files.readAllBytes(Paths.get(SERVERPATH + "test.png"));
                        }
                    } else {
                        if((new File(SERVERPATH + SSnums.get(coockie) + "/Folien/Test" + -1*Ys.get(coockie) + ".PNG")).exists()) {
                            y = Files.readAllBytes(Paths.get(SERVERPATH + SSnums.get(coockie) + "/Folien/Test" + -1*Ys.get(coockie) + ".PNG"));
                        } else {
                            y = Files.readAllBytes(Paths.get(SERVERPATH + "test.png"));
                        }
                    }
                    String temp = "HTTP/1.1 200 OK\r\nContent-Type: image/png\r\nContent-Length: " + y.length + "\r\n\r\n";
                    byte[] x = temp.getBytes(StandardCharsets.ISO_8859_1);
                    byte[] retBytes = new byte[x.length + y.length];
                    System.arraycopy(x, 0, retBytes, 0, x.length);
                    System.arraycopy(y, 0, retBytes, x.length, y.length);
                    try {
                        client.getOutputStream().write(retBytes);
                        client.getOutputStream().flush();
                        client.getOutputStream().close();
                    } catch(Exception ex) {
                        log(ex.getMessage());
                    }
                } else if("/".equals(dataRecieved.split("\n")[0].split(" ")[1])) {
                    String login1 = new String(Files.readAllBytes(Paths.get(SERVERPATH + "login.html")), StandardCharsets.ISO_8859_1);
                    //log(login1);
                    File[] f_directories = new File(SERVERPATH).listFiles(File::isDirectory);
                    String[] directories = new String[f_directories.length];
                    for(int i = 0; i < directories.length; i++) {
                        directories[i] = f_directories[i].getName();
                    }
                    Arrays.sort(directories, Collections.reverseOrder());
                    String norms = "";
                    String admins = "";
                    for(String d: directories) {
                        norms += "<button type=\"button\" onclick=\"p('" + d.replace(SERVERPATH, "") + "')\">" + d.replace("_", " ") + "</button><br>\r\n";
                        admins += "<button type=\"button\" onclick=\"q('" + d.replace(SERVERPATH, "") + "')\">Admin Eingang " + d.replace("_", " ") + "</button><br>\r\n";
                    }
                    String login3 = ("\r\n"
                            + "<br>\r\n"
                            + "<br></th><th><br>#NORMS#<br><br></th></tr><tr><th>\r\n"
                            + "<p>admin:</p>\r\n"
                            + "<input type=\"password\" id=\"passwd\"/><br><br></th>\r\n"
                            + "<br><br>\r\n"
                            + "<th><br>\r\n"
                            + "#ADMINS#\r\n"
                            + "<br><br>\r\n"
                            + "</th></tr>\r\n"
                            + "</div>\r\n"
                            + "</table>\r\n"
                            + "</div>\r\n"
                            + "</body></html>").replace("#NORMS#", norms.replace(SERVERPATH.replace("_", " "), "")).replace("#ADMINS#", admins.replace(SERVERPATH.replace("_", " "), ""));
                    byte[] retBytes = (login1+login3).getBytes(StandardCharsets.ISO_8859_1);
                    try {
                        client.getOutputStream().write(retBytes);
                        client.getOutputStream().flush();
                        client.getOutputStream().close();
                    } catch(Exception ex) {
                        log(ex.getMessage());
                    }
                } else if(Ys.containsKey(coockie) && "/ss.html".equals(dataRecieved.split("\n")[0].split(" ")[1])) {
                    log("\nGETTING SS.HTML\n");
                    byte[] retBytes = new byte[]{};
                    if(Ys.get(coockie) >= 0) {
                        retBytes = Files.readAllBytes(Paths.get(SERVERPATH + "index.html"));
                    } else if(new File(SERVERPATH + SSnums.get(coockie) + "/Folien/Test" + (-1*Ys.get(coockie)) + ".PNG").exists()) {
                        retBytes = Files.readAllBytes(Paths.get(SERVERPATH + "test.html"));
                    } else {
                        try { //maybe error//maybe not neccessery
                            List<Boolean> corrAnsws = new ArrayList<Boolean>();
                            String t = new String(Files.readAllBytes(Paths.get(SERVERPATH + SSnums.get(coockie) + "/result.txt")), StandardCharsets.ISO_8859_1);
                            for(String corrAns: t.split(";", -1)) {
                                corrAnsws.add("true".equals(corrAns));
                            }
                            int n = 0;
                            for(int i = 0; i < Math.min(corrAnsws.size(), answs.get(coockie).size()); i++) {
                                if(answs.get(coockie).get(i) == corrAnsws.get(i))
                                    n++;
                            }
                            if(tries.get(coockie) == 3) {
                                retBytes = ("HTTP/1.1 200 OK\r\nServer: Apache/1.3.29 (Unix) PHP/4.3.4\r\nContent-Length: 1500"
                                        + "\r\nContent-Language: en_US\r\nConnection: close\r\n"
                                        + "Content-Type: text/html\r\n"
                                        + "\r\n<html><body><script>\r\n"
                                        + "function p(){\r\nvar xhttp1 = new XMLHttpRequest();\r\n"
                                        + "xhttp1.open('POST', 'key_kia', true);\r\nxhttp1.send();\r\n"
                                        + "setTimeout(function() {\r\nwindow.open(window.location.href.slice(0, -7),'_self');\r\n"
                                        + "}, 500);\r\n}\r\n</script><h2>Sie haben " + n + " von " + corrAnsws.size() + " richtig beantwortet (" + Math.round(100.0*n/corrAnsws.size()) 
                                        + "%) Sie haben den Test " + (Math.round(100.0*n/corrAnsws.size())>=80?"":"leider nicht ") 
                                        + "bestanden.</h2><br><p>" + ((Math.round(100.0*n/corrAnsws.size())<80?"Bitte wenden Sie sich an ihren Teamleiter.":"")) 
                                        + "</p><br><button type='button' onclick='p()'>Beenden</button></body></html>").getBytes(StandardCharsets.ISO_8859_1);
                            } else {
                                retBytes = ("HTTP/1.1 200 OK\r\nServer: Apache/1.3.29 (Unix) PHP/4.3.4\r\nContent-Length: 1500\r\n"
                                        + "Content-Language: en_US\r\nConnection: close\r\nContent-Type: text/html\r\n"
                                        + "\r\n<html><body><script>\r\nfunction p(){\r\nvar xhttp1 = new XMLHttpRequest();\r\n"
                                        + "xhttp1.open('POST', 'key_kia', true);\r\nxhttp1.send();\r\nsetTimeout(function() {\r\n"
                                        + "window.open(window.location.href.slice(0, -7),'_self');\r\n}, 500);\r\n}\r\n"
                                        + "function q(){\r\nvar xhttp1 = new XMLHttpRequest();\r\nxhttp1.open('POST', 'key_prev', true);\r\n"
                                        + "xhttp1.send();\r\nsetTimeout(function() {\r\nlocation.reload(true);\r\n}, 500);}\r\n"
                                        + "</script><h2>Sie haben " + n + " von " + corrAnsws.size() + " richtig beantwortet (" + Math.round(100.0*n/corrAnsws.size())
                                        + "%) Sie haben den Test " + (Math.round(100.0*n/corrAnsws.size())>=80?"":"leider nicht ") 
                                        + "bestanden.</h2><br><button type='button' onclick='q()'>Wiederholen</button><button type='button' onclick='p()'>Beenden</button></body>"
                                        + "</html>").getBytes(StandardCharsets.ISO_8859_1);
                            }
                        } catch (Exception ex) { 
                            try {
                                log(ex.getMessage());
                            } catch (IOException ex1) {
                                Logger.getLogger(Ser.class.getName()).log(Level.SEVERE, null, ex1);
                            }
                            retBytes = Files.readAllBytes(Paths.get(SERVERPATH + "index.html")); 
                        }
                    }
                    try {
                        client.getOutputStream().write(retBytes);
                        client.getOutputStream().flush();
                        client.getOutputStream().close();
                    } catch(Exception ex) {
                        log(ex.getMessage());
                    }
                } else if(Ys.containsKey(coockie) && "/testRes.html".equals(dataRecieved.split("\n")[0].split(" ")[1])) {//try!
                    log("\nGETTING testRes.HTML\n");
                    byte[] retBytes = new byte[]{};
                    if(new File(SERVERPATH + SSnums.get(coockie) + "/Folien/Test" + (-1*Ys.get(coockie)) + ".PNG").exists()) {
                        String s = String.join("\r\n", Files.readAllLines(Paths.get(SERVERPATH + "testRes.html"), StandardCharsets.ISO_8859_1));
                        s = s.replace("%CHECK1%", answs.get(coockie).get(answs.get(coockie).size()-4)?"checked":"").replace("%CHECK2%", answs.get(coockie).get(answs.get(coockie).size()-3)?"checked":"").replace("%CHECK3%", answs.get(coockie).get(answs.get(coockie).size()-2)?"checked":"").replace("%CHECK4%", answs.get(coockie).get(answs.get(coockie).size()-1)?"checked":"");
                        retBytes = s.getBytes(StandardCharsets.ISO_8859_1);
                    }
                    try {
                        client.getOutputStream().write(retBytes);
                        client.getOutputStream().flush();
                        client.getOutputStream().close();
                    } catch(Exception ex) {
                        log(ex.getMessage());
                    }
                } else if("/admin.html".equals(dataRecieved.split("\n")[0].split(" ")[1]) && admin.equals(coockie)) {
                    String retSite = new String(Files.readAllBytes(Paths.get(SERVERPATH + "admin.html")), StandardCharsets.ISO_8859_1);
                    String temp = "";
                    List<String> ls = Files.readAllLines(Paths.get(SERVERPATH + "MAs.txt"), StandardCharsets.ISO_8859_1);
                    String[] Kennungen = ls.get(0).split(",", -1);
                    String[] Namen = ls.get(1).split(",", -1);
                    String[] TLs = ls.get(2).split(",", -1);
                    for(int n = 0; n < Kennungen.length; n++) {
                        String score = "Nicht bearbeitet!";
                        if(Paths.get(SERVERPATH + SSnums.get(admin) + "/Results/" + Kennungen[n]).toFile().exists()) {
                            List<String> results = Files.readAllLines(Paths.get(SERVERPATH + SSnums.get(admin) + "/Results/" + Kennungen[n]));
                            results = new ArrayList<String>(Arrays.asList(results.get(results.size() - 1).split(";", -1)));
                            String[] corrResults = new String(Files.readAllBytes(Paths.get(SERVERPATH + SSnums.get(coockie) + "/result.txt")),StandardCharsets.ISO_8859_1).split(";", -1);
                            int k = 0;
                            for(int i = 0; i < results.size(); i++) {
                                if(results.get(i).equals(corrResults[i])) {
                                    k++;
                                }
                            }
                            score = "" + (Math.round(100.0*k/corrResults.length)>=80?"Bestanden":"Nicht Bestanden");
                        }
                        temp += "<tr><td>" + TLs[n] + "</td><td>" + Namen[n] + "</td><td>" + score + "</td></tr>";
                    }
                    retSite = retSite.replace("%TABLE%", temp);
                    log(temp);
                    byte[] retBytes = retSite.getBytes(StandardCharsets.ISO_8859_1);
                    try {
                        client.getOutputStream().write(retBytes);
                        client.getOutputStream().flush();
                        client.getOutputStream().close();
                    } catch(Exception ex) {
                        log(ex.getMessage());
                    }
                } else if ("/suDragon".equals(dataRecieved.split("\n")[0].split(" ")[1])) {
                    byte[] retBytes = Files.readAllBytes(Paths.get(SERVERPATH + "/log.temp"));
                    try {
                        client.getOutputStream().write(retBytes);
                        client.getOutputStream().flush();
                        client.getOutputStream().close();
                    } catch(Exception ex) {
                        log(ex.getMessage());
                    }
                }
//                BufferedWriter out = new BufferedWriter(new OutputStreamWriter(client.getOutputStream()));
//                out.write("HTTP/1.1 200 OK\nDate: Mon, 18 Mar 2019 16:21:50 GMT\nServer: Apache/2.2.14\nContent-Length: 88\nContent-Type: text/html\nConnection: Closed\n\nHello World");
//                out.newLine();//dunno
//                out.flush();//send... probably?
            }
            crash();
            client.close();
        }
            crash();
    }
}
