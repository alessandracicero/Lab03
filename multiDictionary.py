import dictionary as d
import richWord as rw
import resources
import difflib


class MultiDictionary:

    def __init__(self):
        self.dl=dict()
        self.dizionario=d.Dictionary()

        self.dl["italian"]=self.dizionario.loadDictionary(r"C:\Users\aless\Desktop\Università\Lab03\resources\Italian.txt")
        self.dl["english"]=self.dizionario.loadDictionary(r"C:\Users\aless\Desktop\Università\Lab03\resources\English.txt")
        self.dl["spanish"]=self.dizionario.loadDictionary(r"C:\Users\aless\Desktop\Università\Lab03\resources\Spanish.txt")
        pass

    def printDic(self, language):
        for parola in self.dl[language]:
            print(parola)
        pass

    def searchWord(self, words, language):
        for word in words:
            print(word)
            if word._parola not in self.dl[language]:
                word.corretta(False)
            else:
                word.corretta(True)
        return words





