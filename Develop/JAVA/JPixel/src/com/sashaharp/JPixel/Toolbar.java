package com.sashaharp.JPixel;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.beans.PropertyChangeListener;

public class Toolbar extends JFrame {
    public static String currTool = "pencil";
    public static Color currColor = Color.black;

    private JPanel tools = new JPanel(new GridLayout(0, 3));
    private JPanel pencil = new CenteredButton(new ToolBtnAction("pencil", "Single pixel drawing tool", KeyEvent.VK_P));
    private JPanel select = new CenteredButton(new ToolBtnAction("select", "Pixel selection tool", KeyEvent.VK_S));
    private JPanel zoom = new CenteredButton(new ToolBtnAction("zoom", "Zooming tool", KeyEvent.VK_Z));
    private JPanel move = new CenteredButton(new ToolBtnAction("move", "Moving/Paning tool", KeyEvent.VK_M));

    private JPanel colors = new JPanel(new GridLayout(0, 5));
    private static ColorButton[] cols = new ColorButton[10];

    public static void getCol(int num) {
        currColor = cols[num].getColor();
    }

    static class CenteredButton extends JPanel {
        private JButton button;
        public CenteredButton(Action a) {
            button = new JButton(a);
            button.setAlignmentX(Component.CENTER_ALIGNMENT);
            button.setAlignmentY(Component.CENTER_ALIGNMENT);
            button.setPreferredSize(new Dimension(20, 20));
            button.setMaximumSize(new Dimension(20, 20));
            button.setMinimumSize(new Dimension(20, 20));
            this.add(button);
        }
    }

    static class ColorButton extends JPanel {
        private JButton button;
        public ColorButton() {
            button = new JButton("");
            ActionListener actionListener = new ActionListener() {
                public void actionPerformed(ActionEvent actionEvent) {
                    Color initialBackground = button.getBackground();
                    Color background = JColorChooser.showDialog(null, "JColorChooser", initialBackground);
                    if (background != null) {
                        button.setBackground(background);
                        Toolbar.currColor = background;
                    }
                }
            };
            button.addActionListener(actionListener);
            this.add(button, BorderLayout.CENTER);
        }
        public Color getColor() {
            return button.getBackground();
        }
    }

    static class ToolBtnAction extends AbstractAction {
        private String name;
        public ToolBtnAction(String text, String desc, Integer mnemonic) {
            super(text);
            putValue(SHORT_DESCRIPTION, desc);
            putValue(MNEMONIC_KEY, mnemonic);
            name = text;
        }
        @Override
        public void actionPerformed(ActionEvent e) {
            Toolbar.currTool = name;
        }
    }

    public Toolbar() {
        super("Toolbar");

        setLayout(new GridLayout(0, 1));

        tools.add(pencil);
        tools.add(select);
        tools.add(zoom);
        tools.add(move);

        this.add(tools);

        for(int n = 0; n < 10; n++) {
            cols[n] = new ColorButton();
            colors.add(cols[n]);
        }
        this.add(colors);

        this.setSize(200, 800);
        this.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        this.setVisible(true);
    }
}
