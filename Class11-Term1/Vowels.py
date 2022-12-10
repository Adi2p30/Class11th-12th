word = input("which word")
vlist = ["a","e","i","o","u","A","E","I","O","U"]
vowels = 0
for i in word:
    if i in vlist:
        vowels = vowels+1
print("Number of Vowels: ", vowels)
