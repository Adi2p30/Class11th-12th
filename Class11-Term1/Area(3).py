shape = input("triangle, circle, square, rectangle")
what = input("What do you want(Perimeter, Area)")
if what == "Perimeter":
    if shape == "Circle":
        r = int(input("radius of circle? "))
        ans = 2*3.14*r
    elif shape == "Square":
        s = int(input("Side? "))
        ans = 4*s
    elif shape == "Rectangle":
        l = int(input("what is length? "))
        b = int(input("what is breadth? "))
        ans = 2 *(l+b)
    elif shape == "Triangle":
        s1 = int(input("what is side1 "))
        s2 = int(input("what is side2 "))
        s3 = int(input("what is side3 "))
        ans = s1+s2+s3
    print("Perimeter of " + shape +" "+ str(ans))

elif what == "Area":
    if shape == "Circle":
        r = int(input("radius of circle? "))
        ans = 3.14 * (r**2)
    elif shape == "Square":
        s = int(input("Side? "))
        ans = s**2
    elif shape == "Rectangle":
        l = int(input("what is length? "))
        b = int(input("what is breadth? "))
        ans = l*b
    elif shape == "Triangle":
        s1 = int(input("what is side1 "))
        s2 = int(input("what is side2 "))
        s3 = int(input("what is side3 "))
        s = (s1+s2+s3)/2
        ans = (s*(s-s1)*(s-s2)*(s-s3))**(1/2)
    print("Area of " + shape +" " +str(ans))
else:
    print("Cant be done in this program")
    exit(1)

