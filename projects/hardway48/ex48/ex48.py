
import re
print re.sub('([bcdfghjklmnpqrstvwxyz])', r'o\1', 'tobias')

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
        try:
            for i in range(len(self.words)):
                if self.words[i] in sentence:
                    list.append(sentence[self.words[i]])
            return list
        except (IOError ,ZeroDivisionError),e:
            return e.message

lexicon=Lexicon()