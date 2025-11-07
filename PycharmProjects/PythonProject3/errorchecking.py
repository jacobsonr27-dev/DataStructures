import time
from stack import Stack

f = open("GoodCode.txt")
code_str = f.read()
Stack = Stack()


for i in code_str:
    if i == '(' or i == ')' or i == '[' or i == ']' or i == '{' or i == '}':
        Stack.push(i)





