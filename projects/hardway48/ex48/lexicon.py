# class Lexicon(object):
#
#     def __init__(self):
#         self.lex={
#             "north":"direction",
#             "south": "direction",
#             "east": "direction",
#             "west": "direction",
#             "up": "direction",
#             "down": "direction",
#             "go":"ver",
#             "kill": "ver",
#             "eat": "ver",
#             "the": "stop",
#             "in": "stop",
#             "of": "stop",
#             "bear": "noun",
#             "princess": "noun",
#             "player": "noun",
#             "3": "number",
#             "91234": "number",
#             "1234": "number",
#             "ASDFADFASDF": "error",
#             "IAS": "error",
#         }
#         self.list=[]
#
#     def scan(self,sentence):
#         self.sentences=sentence
#         self.words=sentence.split()
#         try:
#             for i in range(len(self.words)):
#                 if self.words[i] in sentence:
#                     list.append(sentence[self.words[i]])
#             return list
#         except (IOError ,ZeroDivisionError),e:
#             return e.message
#
# lexicon=Lexicon()

first_directs=(
    ("direction","north"),
    ("direction","south"),
    ("direction","east"),
    ("direction","west"),
    ("direction","down"),
    ("direction","up")
    ("direction","letf"),
    ("direction","right")
    ("direction", "back")
)

second_verbs=(
    ("verb","go"),
    ("verb", "kill"),
    ("verb", "stop"),
    ("verb", "eat"),
)

third_stops=(
    ("stop","the"),
    ("stop", "in"),
    ("stop", "of"),
    ("stop", "from"),
    ("stop", "at"),
    ("stop", "it"),
)

fourth_nouns=(
    ("nouns","door"),
    ("nouns", "bear"),
    ("nouns", "pricess"),
    ("nouns", "cabinet"),
)

fifth_nums=(
    ()
)

sentence=[first_directs,second_verbs,third_stops,fourth_nouns,fifth_nums]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(list,words,sentences):
    list=[]
    words=sentences.split()


