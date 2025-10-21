import time
from stack import Stack

Browser = Stack()
past_sites = Stack()

while True:
    print("Would you like to:")
    time.sleep(0.5)
    print("1 - Go to a new site")
    print("2 - Go back")
    print("3 - Go forward")
    print("4 - Exit")
    action = input()
    if action == '4':
        running = False
    elif action == '1':
        print("What site would you like to visit?")
        newest_site = input()
        time.sleep(0.5)
        print("You are currently browsing "+ newest_site)
        time.sleep(1)
        Browser.push(newest_site)
    elif action == '2':
        if Browser.size() > 0:
            last_site = Browser.pop()
            past_sites.push(last_site)
            current_site = Browser.top()
            print("You are currently browsing " + current_site)
        else:
            print("You can't do that yet.")
    elif action == '3':
        if past_sites.size() > 0:
            last_backed_site = past_sites.pop()
            Browser.push(last_backed_site)
            current_site = Browser.top()
            print("You are currently browsing " + current_site)
        else:
            print("You can't do that yet.")