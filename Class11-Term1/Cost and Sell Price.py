Cost_price = float(input("What is cost price"))
Sell_price = float(input("What is the Sell price"))
if (Sell_price - Cost_price) > 1:
    print("Total profit is: ", Sell_price - Cost_price)
else:
    print("Total loss is: ", Sell_price - Cost_price)