maths = int(input("Maths marks?/80 "))
eng = int(input("English marks?/80 "))
sans = int(input("Sanskrit marks?/80 "))
sci= int(input("Science marks?/80 "))
sst = int(input("SST marks?/80 "))
list = [maths, eng, sans, sci, sst]
for i in range(0,5):
    if list[i-1] > 80:
        print("You cheated")
        exit()
percentage = (maths + eng + sans + sci + sst)/400*100
print("percentage = "+ str((maths + eng + sans + sci + sst)/400*100)+ "%")
if percentage > 80:
    print("You got an A grade")
elif percentage > 60:
    print("You got an B grade")
elif percentage > 40:
    print("You got an C grade")
else:
    print("You failed")
