

class Lexicon(object):

    def __init__(self):
        self.lex={
            "north":"direction",
            "south": "direction",
            "east": "direction",
            "west": "direction",
            "up": "direction",
            "down": "direction",
            "go":"ver",
            "kill": "ver",
            "eat": "ver",
            "the": "stop",
            "in": "stop",
            "of": "stop",
            "bear": "noun",
            "princess": "noun",
            "player": "noun",
            "3": "number",
            "91234": "number",
            "1234": "number",
            "ASDFADFASDF": "error",
            "IAS": "error",
        }
        self.list=[]

    def scan(self,sentence):
        self.sentences=sentence
        self.words=sentence.split()

        for word in self.words:
            if word.isdigit():
                self.list.append(self.sentences[word],int (word))
            else:
                self,list.append(self.sentences[word],word)



lexicon=Lexicon()