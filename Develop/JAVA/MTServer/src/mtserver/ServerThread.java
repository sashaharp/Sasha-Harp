package mtserver;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author sashaharp
 */
public class ServerThread implements Runnable {
    Thread t;
    Database lock;
    int state = 0;
    
    public ServerThread(String name, Database lock) {
        t = new Thread(this, name);
        this.lock = lock;
        this.state = 1;
        t.start();
    }
    
    @Override
    public void run(){
        try {
            MTServer.log("Booting up " + Thread.currentThread().getName() + "\r\n\r\n");
            while(state == 1) {
                String data;
                Socket client;
                String clientAddress;
                BufferedReader in;
                synchronized(lock) {
                    client = lock.server.accept();
                    clientAddress = client.getInetAddress().getHostAddress();

                    in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                    char[] buffer = new char[1000];
                    in.read(buffer);
                    data = String.valueOf(buffer);
                }
                packetInfo info = new packetInfo(data);
                MTServer.log("Thread " + Thread.currentThread().getName() + " is handling " + (info.cookie==""?"a new client":info.cookie) + "\r\n\r\n");
                if(info.get) { //getRequest
                    byte[] retBytes = new byte[]{};
                    if(info.arguments[0].equals("/")) {
                        String login = new String(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + "login.html")), StandardCharsets.ISO_8859_1);
                        File[] f_directories = new File(MTServer.SERVERPATH).listFiles(File::isDirectory);
                        String[] directories = new String[f_directories.length];
                        for(int i = 0; i < directories.length; i++) {
                            directories[i] = f_directories[i].getName();
                        }
                        Arrays.sort(directories, Collections.reverseOrder());
                        String norms = "";
                        String admins = "";
                        for(String d: directories) {
                            norms += "<button type=\"button\" onclick=\"p('" + d.replace(MTServer.SERVERPATH, "") + "')\">" + d.replace("_", " ") + "</button><br>\r\n";
                            admins += "<button type=\"button\" onclick=\"q('" + d.replace(MTServer.SERVERPATH, "") + "')\">Admin Eingang " + d.replace("_", " ") + "</button><br>\r\n";
                        }
                        login = login.replace("#NORMS#", norms.replace(MTServer.SERVERPATH.replace("_", " "), "")).replace("#ADMINS#", admins.replace(MTServer.SERVERPATH.replace("_", " "), ""));
                        retBytes = getAnsw(login.getBytes(StandardCharsets.ISO_8859_1), true, false);
                    } else if(info.arguments[0].equals("/Folie.PNG")) {
                        int n;
                        if((n = lock.contains(info.cookie)) >= 0) {
                            String SSnum = lock.entries.get(n).currentSS;
                            int page = lock.entries.get(n).page;
                            if(page>0) {
                                if((new File(MTServer.SERVERPATH + SSnum + "/Folien/Folie" + page + ".PNG")).exists()) {
                                    retBytes = getAnsw(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + SSnum + "/Folien/Folie" + page + ".PNG")), false, false);
                                } else {
                                    lock.entries.get(n).page++;
                                    retBytes = getAnsw(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + "test.png")), false, false);
                                }
                            } else {
                                if((new File(MTServer.SERVERPATH + SSnum + "/Folien/Folie" + (-1*page) + ".PNG")).exists()) {
                                    retBytes = getAnsw(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + SSnum + "/Folien/Folie" + (-1*page) + ".PNG")), false, false);
                                } else {
                                    retBytes = getAnsw(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + "test.png")), false, false);
                                }
                            }
                        }
                    } else if(info.arguments[0].equals("/ss.html")) {
                        int n;
                        if((n = lock.contains(info.cookie)) >= 0) {
                            int page = lock.entries.get(n).page;
                            if(page >= 0){
                                retBytes = getAnsw(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + "index.html")), true, false);
                            } else {
                                String SSnum = lock.entries.get(n).currentSS;
                                if((new File(MTServer.SERVERPATH + SSnum + "/Folien/Folie" + (-1*page) + ".PNG")).exists()) {
                                    retBytes = getAnsw(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + "test.html")), true, false);
                                } else {
                                    List<Boolean> userAnsws = lock.entries.get(n).answs;
                                    String[] t = new String(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + SSnum + "/result.txt")), StandardCharsets.ISO_8859_1).split(";", -1);
                                    for(int k = 0, l = 0; k < userAnsws.size(); l++, k++) {
                                        if(userAnsws.get(k) == t[l].equals("true")) {
                                            userAnsws.remove(k);
                                            k--;
                                        }
                                    }
                                    if(lock.entries.get(n).tries == 3) {
                                        retBytes = getAnsw(("<html><body><script>\r\n"
                                                + "function p(){\r\nvar xhttp1 = new XMLHttpRequest();\r\n"
                                                + "xhttp1.open('POST', 'key_kia', true);\r\nxhttp1.send();\r\n"
                                                + "setTimeout(function() {\r\nwindow.open(window.location.href.slice(0, -7),'_self');\r\n"
                                                + "}, 500);\r\n}\r\n</script><h2>Sie haben " + userAnsws.size() + " von " + t.length + " richtig beantwortet (" + Math.round(100.0*userAnsws.size()/t.length) 
                                                + "%) Sie haben den Test " + (Math.round(100.0*userAnsws.size()/t.length)>=80?"":"leider nicht ") 
                                                + "bestanden.</h2><br><p>" + ((Math.round(100.0*userAnsws.size()/t.length)<80?"Bitte wenden Sie sich an ihren Teamleiter.":"")) 
                                                + "</p><br><button type='button' onclick='p()'>Beenden</button></body></html>").getBytes(StandardCharsets.ISO_8859_1), true, false);
                                    } else {
                                        retBytes = getAnsw(("<html><body><script>\r\nfunction p(){\r\nvar xhttp1 = new XMLHttpRequest();\r\n"
                                                + "xhttp1.open('POST', 'key_kia', true);\r\nxhttp1.send();\r\nsetTimeout(function() {\r\n"
                                                + "window.open(window.location.href.slice(0, -7),'_self');\r\n}, 500);\r\n}\r\n"
                                                + "function q(){\r\nvar xhttp1 = new XMLHttpRequest();\r\nxhttp1.open('POST', 'key_prev', true);\r\n"
                                                + "xhttp1.send();\r\nsetTimeout(function() {\r\nlocation.reload(true);\r\n}, 500);}\r\n"
                                                + "</script><h2>Sie haben " + userAnsws.size() + " von " + t.length + " richtig beantwortet (" + Math.round(100.0*userAnsws.size()/t.length)
                                                + "%) Sie haben den Test " + (Math.round(100.0*userAnsws.size()/t.length)>=80?"":"leider nicht ") 
                                                + "bestanden.</h2><br><button type='button' onclick='q()'>Wiederholen</button><button type='button' onclick='p()'>Beenden</button></body>"
                                                + "</html>").getBytes(StandardCharsets.ISO_8859_1), true, false);
                                    }
                                }
                            }
                        }
                    } else if(info.arguments[0].equals("testRes.html")) {
                        int n;
                        if((n = lock.contains(info.cookie)) >= 0) {
                            String SSnum = lock.entries.get(n).currentSS;
                            int page = lock.entries.get(n).page;
                            List<Boolean> answs = lock.entries.get(n).answs;
                            if(new File(MTServer.SERVERPATH + SSnum + "/Folien/Test" + (-1*page) + ".PNG").exists() && answs.size() >= 4) {
                                String s = String.join("\r\n", Files.readAllLines(Paths.get(MTServer.SERVERPATH + "testRes.html"), StandardCharsets.ISO_8859_1));
                                s = s.replace("%CHECK1%", answs.get(answs.size()-4)?"checked":"").replace("%CHECK2%", answs.get(answs.size()-3)?"checked":"").replace("%CHECK3%", answs.get(answs.size()-2)?"checked":"").replace("%CHECK4%", answs.get(answs.size()-1)?"checked":"");
                                retBytes = getAnsw(s.getBytes(StandardCharsets.ISO_8859_1), true, false);
                            }
                        }
                    } else if(info.arguments[0].equals("/admin.html")) {
                        int n;
                        if((n = lock.contains(info.cookie)) >= 0 && lock.admin.equals(info.cookie)) {
                            String SSnum = lock.entries.get(n).currentSS;
                            String retSite = new String(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + "admin.html")), StandardCharsets.ISO_8859_1);
                            String temp = "";
                            List<String> ls = Files.readAllLines(Paths.get(MTServer.SERVERPATH + "MAs.txt"), StandardCharsets.ISO_8859_1);
                            String[] Kennungen = ls.get(0).split(",", -1);
                            String[] Namen = ls.get(1).split(",", -1);
                            String[] TLs = ls.get(2).split(",", -1);
                            String[] corrResults = new String(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + SSnum + "/result.txt")),StandardCharsets.ISO_8859_1).split(";", -1);
                            for(int k = 0; k < Kennungen.length; k++) {
                                String score = "Nicht bearbeitet!";
                                if(Paths.get(MTServer.SERVERPATH + SSnum + "/Results/" + Kennungen[n]).toFile().exists()) {
                                    List<String> results = Files.readAllLines(Paths.get(MTServer.SERVERPATH + SSnum + "/Results/" + Kennungen[n]));
                                    if(results.size() > 0) {
                                        results = new ArrayList<String>(Arrays.asList(results.get(results.size() - 1).split(";", -1)));
                                        int l = 0;
                                        for(int i = 0; i < results.size(); i++) {
                                            if(results.get(i).equals(corrResults[i])) {
                                                l++;
                                            }
                                        }
                                        if(results.size() > 0)
                                            score = "" + (Math.round(100.0*l/corrResults.length)>=80?"Bestanden":"Nicht Bestanden");
                                    }
                                }
                                temp += "<tr><td>" + TLs[k] + "</td><td>" + Namen[k] + "</td><td>" + score + "</td></tr>";
                            }
                            retSite = retSite.replace("%TABLE%", temp);
                            retBytes = getAnsw(retSite.getBytes(StandardCharsets.ISO_8859_1), true, false);
                        }
                    } else if(info.arguments[0].equals("/suDragon")) {
                        retBytes = getAnsw(Files.readAllBytes(Paths.get(MTServer.SERVERPATH + "/log.temp")), true, true);
                    }
                    synchronized(lock) {
                        try {
                            client.getOutputStream().write(retBytes);
                            client.getOutputStream().flush();
                            client.getOutputStream().close();
                            MTServer.log(Thread.currentThread().getName() + " has sent a packet successfully\r\n\r\n");
                        } catch(Exception e) {
                            MTServer.log("Error while " + Thread.currentThread().getName() + " was sending answer to last request\r\nerror=" + e.getMessage() + "\r\n\r\n");
                        }
                    }
                } else { //keyRequest
                    if(info.key.equals("login")) {
                        String[] MAs = Files.readAllLines(Paths.get(MTServer.SERVERPATH + "MAs.txt"), StandardCharsets.ISO_8859_1).get(0).split(",", -1);
                        String[] pswds = Files.readAllLines(Paths.get(MTServer.SERVERPATH + "MAs.txt"), StandardCharsets.ISO_8859_1).get(3).split(",", -1);
                        if(Arrays.asList(MAs).contains(info.arguments[0]) && (pswds.length <= Arrays.asList(MAs).indexOf(info.arguments[0]) || pswds[Arrays.asList(MAs).indexOf(info.arguments[0])].equals(info.arguments[1]))) {
                            lock.add(info.arguments[0], 1, info.arguments[2]);
                            MTServer.log("Successful login from " + info.arguments[0] + "\r\n\r\n");
                        } else {
                            MTServer.log("Attempted login from " + info.arguments[0] + " failed\r\n\r\n");
                        }
                    } else if(info.key.equals("next")) {
                        int n;
                        if((n = lock.contains(info.cookie)) >= 0) {
                            int page = lock.entries.get(n).page;
                            if(page > 0) {
                                lock.entries.get(n).page++;
                            } else {
                                lock.entries.get(n).page--;
                            }
                        }
                    } else if(info.key.equals("prev")) {
                        int n;
                        if((n = lock.contains(info.cookie)) >= 0) {
                            int page = lock.entries.get(n).page;
                            String SSnum = lock.entries.get(n).currentSS;
                            if(page > 1) {
                                lock.entries.get(n).page--;
                            } else if(page == 0) {
                                int k = 1;
                                while((new File(MTServer.SERVERPATH + SSnum + "/Folien/Folie" + (n+1) + ".PNG")).exists()) {
                                    n++;
                                }
                                lock.entries.get(n).page = n;
                            } else {
                                if(lock.entries.get(n).tries != 3) {
                                    lock.entries.get(n).page = -1;
                                    lock.entries.get(n).answs = new ArrayList<Boolean>();
                                    lock.entries.get(n).tries++;
                                }
                            }
                        }
                    } else if(info.key.equals("result")) {
                        int n;
                        if((n = lock.contains(info.cookie)) >= 0) {
                            for(String ans: info.arguments[0].split("-", -1)){
                                lock.entries.get(n).answs.add(ans.equals("true"));
                            }
                        }
                    } else if(info.key.equals("kia")) {
                        int n;
                        if((n = lock.contains(info.cookie)) >= 0) {
                            MTServer.log(Thread.currentThread().getName() + " is removing " + info.cookie);
                            List<Boolean> answs = lock.entries.get(n).answs;
                            String SSnum = lock.entries.get(n).currentSS;
                            File f = new File(MTServer.SERVERPATH + SSnum + "/Results/" + info.cookie);
                            if(!f.exists()) {
                                f.createNewFile();
                            }
                            String tempRes = "";
                            for(int k = 0; k < Math.min(Files.readAllLines(Paths.get(MTServer.SERVERPATH + SSnum + "/result.txt"), StandardCharsets.ISO_8859_1).get(0).split(";", -1).length, answs.size()); k++){
                                tempRes += (answs.get(k)?"true":"false") + ";";
                            }
                            synchronized(lock) {
                                Files.write(f.toPath(), ("result:\r\n" + tempRes.substring(0, tempRes.length()-1) + "\r\n").getBytes(), StandardOpenOption.APPEND);
                                lock.entries.remove(n);
                                lock.admin = "123!@#456$%^789&*(";
                            }
                        }
                    } else if(info.key.equals("admin")) {
                        if(info.arguments[0].trim().equals("d534ba14")) {
                            lock.admin = info.cookie;
                            lock.add(info.arguments[0], 0, info.arguments[1]);
                            MTServer.log("Successful login into admin account\r\n\r\n");
                        }
                    }
                }
            }
        } catch (Exception e) {
            MTServer.log("Thread " + Thread.currentThread().getName() + " crashed!\r\nmessege=" + e.getMessage() + "\r\n\r\n");
            state = -1;
        }
    }
    
    private byte[] getAnsw(byte[] answ, Boolean text, Boolean plain) {
        int len = answ.length;
        String header;
        if(text) {
            header = "HTTP/1.1 200 OK\nServer: Apache/1.3.29 (Unix) PHP/4.3.4\nContent-Length: " + len + "\nContent-Language: en_US\nConnection: close\nContent-Type: text/" + (plain?"plain":"html") + "\n\n";
        } else {
            header = "HTTP/1.1 200 OK\nContent-Type: image/png\nContent-Length: " + len + "\n\n";
        }
        byte[] b_h = header.getBytes(StandardCharsets.ISO_8859_1);
        byte[] retBytes = new byte[b_h.length + len];
        System.arraycopy(b_h, 0, retBytes, 0, b_h.length);
        System.arraycopy(answ, 0, retBytes, b_h.length, len);
        return retBytes;
    }
}
