class Stack:
    def __init__(self):
        self.items = []
        self.stack2 = []
    def push(self,value):
        self.items.append(value)
    def pop(self):
        popped_value = self.items.pop()
        return(popped_value)
    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def top(self):
        popped_value = self.items.pop()
        self.items.append(popped_value)
        return popped_value
    def size(self):
        return len(self.items)
    def contains(self,checked_number):
        result = False
        for i in range(len(self.items)):
            popped_value = self.items.pop()
            if popped_value == checked_number:
                result = True
            self.stack2.append(popped_value)
        for i in range(len(self.stack2)):
            popped_value = self.stack2.pop()
            if popped_value == checked_number:
                result = True
            self.items.append(popped_value)
        if result == True:
            return True
        else:
            return False
