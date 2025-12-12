Teams = {}
Matches = {}
f = open("teams", "r")
text = f.readlines()
for i in range(len(text)):
    teams = text[i].split()
    teams[-1] = teams[-1][:-2]
    Matches[str(i+1)] = [[int(teams[0]),int(teams[1]),int(teams[2])],[int(teams[3]),int(teams[4]),int(teams[5])]]
    print(Matches[str(i+1)])


for i in range()

    print("What file would you like me to read?")
    file = input()
    f = open(file + '.txt', "r")
    t = f.read()

    list_of_words = t.split()
    print(list_of_words)

    wordCount = {}
    for i in list_of_words:
        if i in wordCount:
            wordCount[i] += 1
        else:
            wordCount[i] = 1

    print(wordCount)
    for i in wordCount:
        if wordCount[i] > 1:
            print(str(i) + ": " + str(wordCount[i]))