class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return False if self.items else True

    def look(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def contains(self, item):
        contain = False
        for i in range(self.size()):
            a = self.dequeue()
            if a == item:
                contain = True
            self.enqueue(a)
        return contain

    def __str__(self):
        return "Queue containing the items: " + str(self.items)

    def __add__(self, other):
        queue = Queue()

        for i in range(self.size()):
            a = self.dequeue()
            queue.enqueue(a)
            self.enqueue(a)

        for i in range(other.size()):
            a = other.dequeue()
            queue.enqueue(a)
            other.enqueue(a)

        return queue

    def __repr__(self):
        return f"queue = Queue()\nfor i in {self.items}:\n    queue.enqueue(i)"

    def __getitem__(self, index):
        item = None

        for i in range(self.size()):
            a = self.dequeue()
            if i == index:
                item = a
            self.enqueue(a)

        return item

    def __eq__(self, other):
        if self.size() != other.size():
            return False

        equal = True

        for i in range(self.size()):
            a = self.dequeue()
            b = other.dequeue()
            if a != b:
                equal = False
            self.enqueue(a)
            other.enqueue(b)

        return equal

    def __contains__(self, item):
        return self.contains(item)