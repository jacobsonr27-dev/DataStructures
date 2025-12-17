class Node:

    def __init__(self, val = None, s = None):
        self.left_child = None
        self.right_child = None
        if s == None:
            self.value = val
        else:
                interior = s[1:-1]
                if "{" not in interior:
                    self.value = interior
                else:
                    b = interior.index("{")
                    child = interior[b:]
                    if interior[b - 8:b] == ", Left: ":
                        self.value = interior[:b - 8]
                        num_brackets = 0
                        for i in range(len(child)):
                            if child[i] == "{":
                                num_brackets += 1
                            elif child[i] == "}":
                                num_brackets -= 1
                                if num_brackets == 0:
                                    break
                        self.left_child = Node(s = child[:i + 1])
                        interior = child[i + 1:]
                        if interior == "":
                            return
                        else:
                            self.right_child = Node(s = interior[9:])
                    else:
                        self.value = interior[:b - 9]
                        self.right_child = Node(s = interior[b:])


    def set_left(self,n):
        self.left_child = n

    def set_right(self,n):
        self.right_child = n

    def set_value(self,val):
        self.value = val

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def get_value(self):
        return self.value

    def is_leaf(self):
        if self.right_child == None and self.left_child == None:
            return True
        else:
            return False

    def __str__(self):
        s = "{" + str(self.get_value())
        if self.get_left() != None:
            s = s + ", Left: " + str(self.get_left())
        if self.get_right() != None:
            s = s + ", Right: " + str(self.get_right())
        s = s + "}"
        return s

class BinaryTree:
    def __init__(self, n = None, s = None):
        if s == None:
            self.root = n
        else:
            string = s[7:-1]
            self.root = Node(string)

    def get_root(self):
        return self.root

    def __str__(self):
        return "Tree: " + str(self.get_root())


