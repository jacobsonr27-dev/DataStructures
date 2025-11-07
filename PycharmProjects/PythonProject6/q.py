import copy


class Queue:
    def __init__(self):
        self.stuff = []

    def enqueue(self,other):
        self.stuff.append(other)

    def dequeue(self):
        return self.stuff.pop(0)

    def empty(self) -> bool:
        return len(self.stuff) == 0

    def look(self):
        return self.stuff[0]

    def size(self) -> int:
        return len(self.stuff)

    def contains(self,has):
        h = copy.copy(self)
        runcon = False
        for i in range(0,self.size()):
            b = self.dequeue()
            if b == has:
                runcon = True
            self.enqueue(b)

        return runcon

    def __str__(self):
        full = "["
        for i in range(0,self.size()):
            b = self.dequeue()
            full = full + b + ","
            self.enqueue(b)

        return full + "]"

    def __add__(self, other):
        toRet = Queue()

        for i in range(0,self.size()):
            toRet.enqueue(self.dequeue())
        for i in range(0,other.size()):
            toRet.enqueue(other.dequeue())

        return toRet

    def __repr__(self):
        return "c = Queue() \nb = "+self.__str__()+"\n"+"for i in range(0,b.size()):\n\tc.enqueue(b[i])"

    def __getitem__(self, item):
        return self.stuff[item]

    def __eq__(self, other):
        return self.stuff == other.stuff