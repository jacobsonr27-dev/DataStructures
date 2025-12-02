class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
    def get_value(self):
        return self.value
    def set_next(self,n):
        self.next = n
    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None






    def __str__(self):
        s = "["
        n = self.head
        while n != None:
            if type(n.get_value()) == str:
                s += '"' + n.get_value() + '", '
            else:
                s += str(n.get_value()) + ", "
            n = n.get_next()
        if s != "[":
            s = s[:-2]
        s = s + "]"
        return s

    def insert_at_start(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length = self.length+1
    def insert_at_end(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length = self.length + 1
    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def delete_at_start(self):
        if self.head.get_next():
            self.head = self.head.get_next()
            self.length = self.length - 1
        else:
            self.head = None
            self.tail = None
            self.length = 0
    def __len__(self):
        return self.length

    def __getitem__(self,ind):
        current = self.head
        for i in range(ind):
            if ind >= len(self):
                raise IndexError
            else:
                current = current.get_next()
        return current.get_value()

    def get_node(self,ind):
        current = self.head
        for i in range(ind):
            if ind >= len(self):
                raise IndexError
            else:
                current = current.get_next()
        return current

    def insert(self, ind, val):
        if ind == 0:
            self.insert_at_start(val)
        elif (ind) >= len(self):
            self.insert_at_end(val)
        else:
            new_node = Node(val)
            current = self.get_node(ind-1)
            current2 = self.get_node(ind)
            current.set_next(new_node)
            new_node.set_next(current2)
            self.length = self.length +1

    def delete_at_end(self):
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return
        else:
            self.tail = self.get_node(len(self)-2)
            self.tail.set_next(None)
            self.length = self.length -1

    def delete(self,ind):
        if ind == 0:
            self.delete_at_start()
        elif ind == len(self)-1:
            self.delete_at_end()
        elif ind >= len(self):
            raise IndexError
        else:
            self.get_node(ind-1).set_next(self.get_node(ind+1))
            self.length = self.length - 1

    def __contains__(self, item):
        check = False
        for ind in range(len(self)):
            current = self.get_node(ind)
            if current.get_value() == item:
                check = True
        return check





