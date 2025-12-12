help_dict = {"file reading": 'Use the following syntax to open a file named example.txt:\nf = open("example.txt", "r")\nThis will make f a file object. To find out the contents of the file, use this:\nt = f.read()',
    "list of words": 'Use the split function to turn a string into a list of words, like this:\ns = "Hello this is Mr. L"\nprint(s.split())',
    "create dictionary": 'Create an empty dictionary with {} (just like [] creates an empty list).',
    "add to dictionary": 'If I wanted to add the key "apples" with a value of 4 to the dictionary, I\'d do it like this:\nd = {}\nd["apples"] = 4',
    "find value": 'If I wanted to find the value of "apples" in a dictionary d, I\'d do this: print(d["apples"])',
    "get keys": 'You can get all the keys in a dictionary d with the following syntax:\nk = d.keys()\nThis creates a keys object. To turn it into a list, just say:\nk = list(k)',
    "get values": 'Getting all the values in a dictionary is similar to getting all the keys, but you use the values() method instead.',
    "size": 'The len() function works on dictionaries.',
    "contains": 'The \'in\' operator works on dictionaries. For instance, the following program will print True:\nd = {}\nd["apples"] = 4\nprint("apples" in d)'
    }
topics = ""
for k in help_dict.keys():
    topics += k + ", "
topics = topics[:-2]
while True:
    print("Valid topics: " + topics)
    print("Please enter a topic and I'll tell you more about it:")
    q = input()
    print()
    if q in help_dict:
        print(help_dict[q])
    elif q == "exit":
        break
    else:
        print("Invalid topic.")
    print()
