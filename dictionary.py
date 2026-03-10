import resources
class Dictionary:
    def __init__(self):
        self._dict = set()

        pass

    def loadDictionary(self,path):
        with open(path, 'r', encoding="utf8") as f:
            lines = f.read().splitlines()
            for line in lines:
                line = line.strip()
                self.dict.add(line)
        return self.dict
        pass

    def printAll(self):
        for parola in self.dict:
            print(parola)


        pass


    @property
    def dict(self):
        return self._dict

