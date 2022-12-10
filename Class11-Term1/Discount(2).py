cost = float(input("What was the cost of the item? "))
discount = float(input("What was the discount applied? "))
discountedprice = float(cost - (discount*cost/100))
print(discountedprice)
