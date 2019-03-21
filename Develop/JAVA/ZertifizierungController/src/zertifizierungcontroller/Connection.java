/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zertifizierungcontroller;

import java.util.HashMap;

/**
 *
 * @author sashaharp
 */
public class Connection {
    public String ip;
    public String name;
    public String password;
    public HashMap QA;
    public javax.swing.JRadioButton connected;
    public static Connection open(String data, String ip) {
        Connection out = new Connection();
        out.ip = ip;
        System.out.println("ip:       " + ip);
        out.name = data.split("\n")[0].trim();
        System.out.println("name:     " + out.name);
        out.password = data.split("\n")[1].trim();
        System.out.println("password: " + out.password);
        out.QA = new HashMap();
        return out;
    }
}
