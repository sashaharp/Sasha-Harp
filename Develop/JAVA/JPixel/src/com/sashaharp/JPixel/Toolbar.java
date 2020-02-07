package com.sashaharp.JPixel;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;

public class Toolbar extends JFrame {
    public static String currTool = "pencil";

    private JPanel tools = new JPanel(new GridLayout(0, 3));
    private JPanel pencil = new CenteredButton(new ToolBtnAction("pencil", "Single pixel drawing tool", KeyEvent.VK_P));
    private JPanel select = new CenteredButton(new ToolBtnAction("select", "Pixel selection tool", KeyEvent.VK_S));
    private JPanel zoom = new CenteredButton(new ToolBtnAction("zoom", "Zooming tool", KeyEvent.VK_Z));
    private JPanel move = new CenteredButton(new ToolBtnAction("move", "Moving/Paning tool", KeyEvent.VK_M));

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

        this.setSize(200, 600);
        this.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        this.setVisible(true);
    }
}
