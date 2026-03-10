import time

import multiDictionary as md
import richWord


class SpellChecker:

    def __init__(self):
        self.parole=list()
        self.dict=md.MultiDictionary()


        pass

    def handleSentence(self, txtIn, language):
        self.start=time.time()
        text=replaceChars(txtIn)
        self.words=text.split(" ")
        for word in self.words:
            rw1=richWord.RichWord(word.lower())
            print(rw1.corretta)
            self.parole.append(rw1)
        self.parole=self.dict.searchWord(self.parole,language)










        pass

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
