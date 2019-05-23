try:
    from tkinter import *
except Exception:
    from Tkinter import *

class QnA():
    def __init__(self, word, meaning, result, rev = False):
        self.word = word
        self.meaning = meaning
        self.result = result
        self.rev = rev
        self.root = Tk()
        self.l = Label(self.root, text=("What is the meaning of " + word + "?") if not rev else ("What is the word for " + meaning + "?"))
        self.l.pack()
        self.i = Entry(self.root)
        self.i.pack()
        self.b = Button(self.root, command=self.check_answer, text="submit")
        self.b.pack()
        self.root.mainloop()
        
    def check_answer(self):
        if self.i.get() == (self.meaning if not self.rev else self.word):
            self.result[0] = 1
        else:
            self.result[0] = 0
        self.root.destroy()

class wordAdder():
    def __init__(self, result):
        self.result = result
        self.root = Tk()
        self.l = Label(self.root, text = "Would you like to add more words?")
        self.l.grid(columnspan=2)
        self.b = Button(self.root, command=self.yes, text="Yes")
        self.b.grid(row=1, column=0)
        self.b = Button(self.root, command=self.no, text="No")
        self.b.grid(row=1, column=1)
        self.root.mainloop()
    def getNumWind(self):
        self.root = Tk()
        self.l = Label(self.root, text="How many words would you like to add?")
        self.l.grid(columnspan=2)
        self.i = Entry(self.root)
        self.i.insert(0, "5")
        self.i.grid(columnspan=2, row=1)
        self.b = Button(self.root, command=self.gotNum, text="Submit")
        self.b.grid(columnspan=2, row=2)
        self.root.mainloop()
    def getAWord(self):
        self.root = Tk()
        self.l = Label(self.root, text="word:   ")
        self.l.grid(row=0,column=0)
        self.l2 = Label(self.root, text="meaning:")
        self.l2.grid(row=0,column=1)
        self.i = Entry(self.root)
        self.i.grid(row=1,column=0)
        self.i2 = Entry(self.root)
        self.i2.grid(row=1,column=1)
        self.b = Button(self.root, command=self.saveWord, text="Submit")
        self.b.grid(columnspan=2, row=2)
        self.root.mainloop()
    def yes(self):
        self.root.destroy()
        self.getNumWind()
    def no(self):
        self.root.destroy()
    def gotNum(self):
        n = int(self.i.get())
        self.root.destroy()
        for i in range(n):
            self.getAWord()
            self.result[self.w] = self.m
    def saveWord(self):
        self.w = self.i.get()
        self.m = self.i2.get()
        self.root.destroy()

class myButton(Button):
    def __init__(self, root, delList, delNum):
        self.delList = delList
        self.delNum = delNum
        super().__init__(root, text="x", command=self.Del, bg="red")
    def Del(self):
        self.delList[self.delNum] = not self.delList[self.delNum]
        if self.delList[self.delNum]:
            self.configure(bg="green", text="o")
        else:
            self.configure(bg="red", text="x")
class dispDict():
    def __init__(self, d, m, o):
        self.root = Tk()
        for w, k in zip(d, range(len(m))):
            l1 = Label(self.root, text=w)
            l1.grid(row=k, column=0)
            l1 = Label(self.root, text=d[w])
            l1.grid(row=k, column=1)
            b = myButton(self.root, o, k)
            b.grid(row=k, column=2)
        self.root.mainloop()
class hub():
    def __init__(self, o):
        self.o = o
    def show(self):
        self.root = Tk()
        Button(self.root, text="Dictionary", command=self.dictionary).pack()
        Button(self.root, text="Sleep", command=self.root.destroy).pack()
        self.root.mainloop()
    def dictionary(self):
        self.o[0] = 1
        self.root.destroy()

if __name__ == "__main__":
    # res = [-1]
    # qna = QnA("Hallo", "Hello", res, True)
    # print(res)
    # d = {}
    # wa = wordAdder(d)
    # print(d)
    d = {"x1":"x2", "x2":"x3"}
    o = [0, 0]
    oo = [False, False]
    dd = dispDict(d, o, oo)
    print(oo)