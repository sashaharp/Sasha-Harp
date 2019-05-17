package snake;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.WindowEvent;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JFrame;
import javax.swing.JTextPane;

/**
 * @author sashaharp
 */
public class Snake extends JFrame implements KeyListener {
    char width = 40;
    char height = 24;
    List<Short> Snakes;
    List<Short> Apples;
    char[][] s;
    Short direction;
    static double freq = 1.5;
    static boolean r = true;
    
    public static void main(String[] args) throws IOException, InterruptedException {
        Snake s = new Snake();
        while(r) {
            s.draw();
            s.update();
            Thread.sleep((long)Math.round(1000.0/freq));
        }
    }
    
    JTextPane j;
    public Snake() {
        super("title");
        
        Snakes = new ArrayList<>();
        Snakes.add((short)(20<<8 + 12));
        Snakes.add((short)(20<<8 + 13));
        Snakes.add((short)(20<<8 + 14));
        Apples = new ArrayList<>();
        s = new char[width][height];
        int t = 0;
        for(char i = 0; i < width; i++){
            for(char j = 0; j < height; j++) {
                if(t < 3 && Snakes.contains(n)) {
                    s[i][j] = '#';
                    t++;
                } else {
                    s[n] = ' ';
                }
            }
        }
        
        setBounds(0, 0, 640, 480);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        j = new JTextPane();
        j.setBackground(Color.BLACK);
        j.setForeground(Color.LIGHT_GRAY);
        j.setFont(new Font("courier", Font.BOLD, 15));
        j.setEnabled(false);
        setFocusable(true);
        requestFocusInWindow();
        this.addKeyListener(this);
        getContentPane().add(j);
        setVisible(true);
    }
    
    public void update() {
        
    }
    
    public void draw() {
        j.setText(new String(s));
    }

    @Override
    public void keyPressed(KeyEvent ke) {
        if(ke.getKeyChar() == 'x') {
            Snake.r = false;
            setVisible(false);
            dispose();
        }
    }

    @Override
    public void keyTyped(KeyEvent ke) { }
    @Override
    public void keyReleased(KeyEvent ke) { }
}
