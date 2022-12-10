elementsno = int(input("How many elements do you want?(>3) "))
elements = [ ]
if elementsno > 3:
    for i in range(0,elementsno):
        inputno = int(input("Input Value number " + str(i+1) + " "))
        elements.append(inputno)
    elements.sort()
    print(elements)
    print("third largest number is " + str(elements[elementsno-3]))
    print("third smallest number is " + str(elements[2]))
else:
    print("list has to be bigger than 3")
    exit(1)
