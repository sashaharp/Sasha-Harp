/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zertifizierungcontroller;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author sashaharp
 */
public class Ser extends Thread {
    private static ServerSocket server;
    public boolean Running;
    public Connection[] connections;
    public int initOrder = 0;
    public static Ser ver;

    Ser(int num) {
        ver = this;
        this.Running = true;
        connections = new Connection[num];
        
    }
    
    @Override
    public void run() {
        try {
            server = new ServerSocket(8888, 10, InetAddress.getLoopbackAddress());//getLocalAddress()
            listen();
        } catch (Exception ex) {
            Logger.getLogger(Ser.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    
    private void listen() throws Exception {
        boolean b = true;
        while(b) {
            String data = null;
            Socket client = server.accept();
            String clientAddress = client.getInetAddress().getHostAddress();
            System.out.println("\r\nNew connection from " + clientAddress);

            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            char[] buffer = new char[1000];
            in.read(buffer);
            System.out.println(buffer);

            /*BufferedWriter out = new BufferedWriter(new OutputStreamWriter(client.getOutputStream()));
            out.write("HTTP/1.1 200 OK\nDate: Mon, 18 Mar 2019 16:21:50 GMT\nServer: Apache/2.2.14\nContent-Length: 88\nContent-Type: text/html\nConnection: Closed\n\nHello World");
            out.newLine();//dunno
            out.flush();//send... probably?
            server.close();
            mainWindow.running=false;
            System.out.println("Closing server");*/

            String Message = String.valueOf(buffer);
            System.out.println(Message);
            if("login-request".equals(Message.split("\n\n")[0].trim())) {
                String[] reqData = Message.split("\n\n")[1].trim().split("\n");
                for(Connection connection : connections) {
                    System.out.println("connection-check: " + connection.name + "=?" + reqData[0].trim() + " : " + connection.password + "=?" + reqData[1].trim());
                    if((connection.name == null ? reqData[0].trim() == null : connection.name.equals(reqData[0].trim())) && (connection.password == null ? reqData[1].trim() == null : connection.password.equals(reqData[1].trim()))) {
                        System.out.println("success");
                        connection.ip = clientAddress;
                        connection.connected.setSelected(true);
                        break;
                    }
                }
            }
        }
    }
}
