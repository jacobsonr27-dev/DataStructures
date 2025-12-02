from linkedlist import *
b = LinkedList()
b.insert(0, "m")
b.insert(0, "o")
b.insert(2, "u")
b.insert(3, "r")
b.insert(0, "c")
b.insert(4, "e")
b.insert(3, "p")
b.insert(5, "t")
assert not b.empty()
assert len(b) == 8

computer = ""
for i in range(8):
    computer += b[i]
print("computer is " + computer)

print("insert() works as intended.")
b.insert(8, "s")
b.delete_at_end()
computer = ""
for i in range(8):
    computer += b[i]
assert computer == "computer"
a = LinkedList()
a.insert(0, "q")
a.insert(1, "u")
a.delete_at_end()
print(a.head)
print(a.tail)
assert a.head == a.tail
a.delete_at_end()
assert a.head == None
assert a.tail == None

print("delete_at_end() works as intended.")

b.delete(6)
b.delete(6)
b.delete(0)
b.delete(1)
b.delete(1)
assert len(b) == 3

out = ""
for i in range(3):
    out += b[i]
print("out is " + out)
assert out == "out"
print("delete() works as intended.")

assert "t" in b
assert "t" in b
assert "o" in b
assert "u" in b
assert "c" not in b
print("__contains__() works as intended.")
