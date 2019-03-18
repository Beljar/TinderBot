import time
from threading import Thread, Event

class Dprint:

    def __init__(self):
        self.tread = None
        self.stop = 0

    def print(self,st):
        if len(st)<=79:
            print(" "*79,  end="\r")
            print(st,   end="\r")
        else:
            raise Exception("Too long string")

    def end(self):
        self.stop = 1
        if self.tread:
            self.tread.join()
        print(" "*79,  end="\r")
        #print("")

    def pulse(self):
        self.stop = 0
        self.tread = Thread(target=self.pulsePrint)
        self.event = Event()
        self.tread.start()

    def genPulseString(self,pos,length):
        st = " " * length
        ls = list(st)
        ls[pos] = "-"
        st = "".join(ls)
        return st
        
    def pulsePrint(self):
        while not self.stop:
            k = 5
            for i in range(2*k-2):
                if self.stop:
                    break
                p = (i>=k)*(k-i-2) + (i<k)*i
                #time.sleep(0.2)
                self.event.wait(timeout=0.2)
                self.print(self.genPulseString(p,k))
                self.event.wait(timeout=0.2)
                #time.sleep(0.2)
''' dp = Dprint()
dp.pulse()
time.sleep(5)
print("test")
time.sleep(5)
dp.end() '''