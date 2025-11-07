from queue import Queue
import time

line = Queue()
customers = int(input("Enter number of customers: "))
customer = 2
ticks = 1


line.enqueue("Customer 1")
while not line.empty():

    ticks+=1
    if ticks % 5 == 0 and customer <= customers :
        line.enqueue(f"customer {customer}")
        customer += 1
    if ticks % 12 == 0 and not line.empty():
        print("Cashier 1 served " + line.dequeue())
    if ticks % 19 == 0 and not line.empty():
        print("Cashier 2 served " + line.dequeue())
    if ticks % 25 == 0 and not line.empty():
        print("Cashier 3 served " + line.dequeue())
    time.sleep(0.0000001)
print(f"total {ticks}")
