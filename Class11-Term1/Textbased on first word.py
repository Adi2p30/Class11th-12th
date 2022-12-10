sentence = input("Enter a sentence: ")
setence = sentence.split(" ")
letter = input("letter by which you want to get words: ")
print(setence)
for i in setence:
    if i[0] == letter:
        print(i)
