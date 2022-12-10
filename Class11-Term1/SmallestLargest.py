elementsno = int(input("How many elements do you want? "))
elements = [ ]
# for i in range(0,elementsno):
#     inputno = int(input("Input Value number " + str(i+1) + " "))
#     elements.append(inputno)
# elements1 = elements.sort()
# print("largest number is " + str(elements1[elementsno-1]))
# print("smallest number is " + str(elements1[0]))

for i in range(0,elementsno):
    inputno = int(input("Input Value number " + str(i+1) + " "))
    elements.append(inputno)
print(elements)
elements.sort()
print("largest number is " + str(elements[elementsno-1]))
print("smallest number is " + str(elements[0]))