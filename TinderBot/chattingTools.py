import csv

class Message:
    IN = 0
    OUT = 1
    def __init__(self,direction,txt):
        self.direction = direction
        self.txt = txt

class Dialog:
    def __init__(self):
        self.messages = []
        self.lastAnsweredMessages = {Message.IN:None,Message.OUT:None}
        self.isEmpty = True
        self.lastMessage = None
    def addMessage(self, message):
        if self.lastMessage:
            if self.lastMessage.direction != message.direction:
                self.lastAnsweredMessages[self.lastMessage.direction] = self.lastMessage
        self.lastMessage = message
        self.messages.append(message)
        self.isEmpty = False
    def getLastAnsweredMessage(self, direction):
        if self.lastAnsweredMessages[direction]:
            return self.lastAnsweredMessages[direction].txt
        else:
            return None
    def getReply(self, pattern):
        if self.isEmpty:
            return pattern.getFirst()
        if self.lastMessage.direction == Message.OUT:
            return pattern.getNext(self.lastMessage.txt, 0)
        else:
            lastAnswered = self.getLastAnsweredMessage(Message.OUT)
            if lastAnswered:
                return pattern.getNext(lastAnswered,1)
            else:
                return pattern.getFirst()

class Pattern:
    def __init__(self,pattern=()):
        self.pattern = pattern
    def importFromCSV(self,path):
        self.pattern = []
        with open(path,"r",encoding="utf-8-sig") as f:
            reader = csv.reader(f, delimiter = "|", quotechar = '"')
            for row in reader:
                lst = tuple(i for i in row)
                self.pattern.append(lst)
        self.pattern = tuple(self.pattern)
        return self.pattern
    def getNext(self, message, wasAnswered):
        for idx in range(len(self.pattern)-1,-1,-1):
            if message in self.pattern[idx]:
                idx2 = self.pattern[idx].index(message)
                if len(self.pattern[idx])>idx2+1:
                    return (self.pattern[idx][idx2+1],)
                elif len(self.pattern) > idx+1 and wasAnswered:
                    return self.pattern[idx+1]
                else:
                    return None
    def getFirst(self):
        return self.pattern[0]


"""test"""
''' pattern = Pattern()
pattern.importFromCSV("SpamScript.csv")
d = Dialog()
rep = d.getReply(pattern)[0]
m = Message(Message.OUT, rep)
d.addMessage(m)
print(rep)
rep = d.getReply(pattern)
m = Message(Message.IN,"bb")
d.addMessage(m)
print(d.getReply(pattern)) '''