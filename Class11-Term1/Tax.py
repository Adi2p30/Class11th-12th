Orignal_price=float(input("Enter Orignal Price:-"))
Total_price= float(input("Enter Total Price:-"))
GST = Total_price - Orignal_price
GST_percentage = ((GST * 100) / Orignal_price)
print("GST Rate = ",GST_percentage )
print("GST Amount = ",GST)