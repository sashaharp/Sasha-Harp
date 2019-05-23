from javax.swing import JFrame, JLabel, JButton, JTextField, JPanel, SwingConstants
from java.awt import GridLayout
import time

class QnA():
    def __init__(self, word, meaning, result, rev = False):
        self.word = word
        self.meaning = meaning
        self.result = result
        self.rev = rev
        self.frame = JFrame("Dictionary", defaultCloseOperation=JFrame.DISPOSE_ON_CLOSE, size=(300,300))
        self.panel = JPanel(GridLayout(0,1))
        self.frame.add(self.panel)
        self.label = JLabel(("What is the meaning of " + word + "?") if not rev else ("What is the word for " + meaning + "?"), SwingConstants.RIGHT)
        self.panel.add(self.label)
        self.input = JTextField("", 15)
        self.panel.add(self.input)
        self.button = JButton("Submit", actionListener=self.onSubmit)
        self.panel.add(self.button)
        self.frame.pack()
        self.frame.visible = True
        self.waitForExec()
    def onSubmit(self, evt):
        if self.input.getText() == (self.meaning if not self.rev else self.word):
            self.result[0] = 1
        else:
            self.result[0] = 0
        self.frame.dispose()
        self.frame = None
    def waitForExec(self):
        while(self.frame is not None):
            time.sleep(2)

if __name__ == "__main__":
    t = [-1]
    QnA("Hallo", "Hello", t, False)
    print(t)