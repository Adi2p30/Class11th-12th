Principle = int(input("Principle? "))
Rate = int(input("Rate of Interest? "))
Time = int(input("What is the TIme period? "))
def SI(P, R, T):
    return(str((P*R*T)/100))

def CI(P,R,T):
    return((P*((1+(R/100))**T)))
print("Simple Interest = " + str(SI(Principle, Rate, Time)))
print("Compound Interest = " + str(CI(Principle, Rate, Time)))