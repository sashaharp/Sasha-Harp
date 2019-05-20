PYNO = 2

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

try:
    input = raw_input
except NameError:
    PYNO = 3

import random

class word():
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        #self.attributes = []
        self.mastery = 0
        self.to = 0
        self.inverse = False

class vocab():
    def __init__(self):
        self.words = []
    def add(self, w):
        self.words.append(w)
    def getToDo(self):
        for w in self.words:
            if w.to == 0:
                return True
        return False
    def save(self):
        with open("save.pk1", "wb") as output:
            pickle.dump(self.words, output, 0)
    def load(self):
        try:
            with open("save.pk1", "rb") as inp:
                self.words = pickle.load(inp)
        except Exception:
            pass
    def getDict(self):
        d = {}
        for w in self.words:
            d[w.word] = w.meaning
        return d

class ioSys():
    def __init__(self):
        self.v = vocab()
        self.v.load()
    def tick(self):
        print("Would you like to add more words? [Y]es or [N]o")
        if(input().capitalize()[0] == "Y"):
            self.getBatch()
            self.v.save()
        for w in self.v.words:
            w.to = max(0, w.to-1)
        while self.v.getToDo():
            for w in random.shuffle(self.v.words):
                if w.to == 0:
                    if self.ask(w):
                        if(w.mastery == 11 and not w.inverse):
                            w.mastery = 0
                            w.inverse = True
                            w.to = 0
                        else:
                            w.to = min(w.mastery, 24*2*3)
                            w.mastery+=1
                    else:
                        w.mastery = max(0, w.mastery - 1)
                        w.to = w.mastery
        self.v.save()
    def ask(self, w):
        if w.inverse:
            print("What is the word for " + w.meaning + "? ")
            if w.word == input():
                print("Correct!\r\n")
                return True
            print("Incorrect. The word for " + w.word + " is " + w.word + ".\r\n")
        else:
            print("What does " + w.word + " mean? ")
            if w.meaning == input():
                print("Correct!\r\n")
                return True
            print("Incorrect. " + w.word + " means " + w.meaning + ".\r\n")
        return False
    def getBatch(self):
        print("The recomended batch size is 5 words. Would You like to add a custom amount? [Y]es or [N]o")
        numWords = 5
        if(input().capitalize()[0] == "Y"):
            try:
                numWords = int(input("How many words would you like to add? "))
            except TypeError:
                print("What you have entered was not a number. proceeding with a batch of 5.\r\n")
        print("please input words as follows: word, meaning.\r\nExample: Apfel, apple")
        for n in range(numWords):
            x = input(str(n+1) + ") ")
            self.v.add(word(x.split(",")[0].strip(), x.split(",")[1].strip()))

def whileAwaits(stopCond, io):
    while(stopCond[0]):
        time.sleep(1)
        print("Would you like to see the dictionary? [Y]es or [N]o")
        if(input().capitalize()[0] == "Y"):
            print(io.v.getDict())


if __name__ == "__main__":
    import threading
    import time
    io = ioSys()
    while True:
        io.tick()
        s = [True]
        t1 = threading.Thread(target=whileAwaits, args=(s,io))
        t1.start()
        time.sleep(60*30)
        s[0] = False
        t1.join()