n = int(input("How many number of multiples: "))
no = int(input("Which number? "))
nolist = []
for i in range(0,n):
    nolist.append(no*i)
print(nolist)
