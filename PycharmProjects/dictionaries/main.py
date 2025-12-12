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