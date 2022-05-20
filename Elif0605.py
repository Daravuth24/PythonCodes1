customer_name = input("Your Name is:")
unit = int(input("Amount You Consumed:"))
if unit > 500:
    price = 3500.00
elif unit > 400:
    price = 3100.00
elif unit > 300:
    price = 2750.00
elif unit > 200:
    price = 1800.00
else:
    price = 720
print("Customer name:",customer_name)
print("Units Consumed:",unit)
print("Price per unit",price,"Riels")
print("Amount to pay:",unit*price,"Riels")