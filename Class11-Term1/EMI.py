p = float(input("Enter the principal:"))
r = float(input("Enter the rate of interest:"))
t = float(input("Enter the time:"))
r = r / (12 * 100)
t = t * 12
EMI = (p * r * (1 + r)**t) / ((1 + r)**t - 1)
print("Monthly EMI is: ", EMI)