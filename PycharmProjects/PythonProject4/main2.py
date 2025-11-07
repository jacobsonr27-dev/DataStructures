from queue import Queue
import time

line1 = Queue()
line2 = Queue()
line3 = Queue()

customers = int(input("Enter number of customers: "))
customer = 2
ticks = 1

while not line1.empty() or not line2.empty() or not line3.empty():
    ticks+=1
    if ticks % 5 == 0 and customer <= customers:
        if line1.size <= line2 and line1.size <= line3.size:
            line1.enqueue(f"customer {customer}")
        elif line2.size <= line1 and line2.size <= line3.size:
            line2.enqueue(f"customer {customer}")
        elif line3.size <= line1 and line3.size <= line2.size:
            line3.enqueue(f"customer {customer}")
        customer += 1
    if ticks % 12 == 0 and not line1.empty():
        print("Cashier 1 served " + line1.dequeue())
    if ticks % 19 == 0 and not line2.empty():
        print("Cashier 2 served " + line2.dequeue())
    if ticks % 25 == 0 and not line3.empty():
        print("Cashier 3 served " + line3.dequeue())
    time.sleep(0.0000001)
print(f"total {ticks}")