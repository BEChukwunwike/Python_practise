membership = True
purchase = 250

# Nested conditional
if membership:
    if purchase >= 100:
        print("Discount = $" + str(purchase * 0.2))
    else:
        print("Discount does not apply to purchase less than $100")
else:
    print("Only members are eligible for discounts")

# Refactored code
if membership and purchase >= 100:
    print("Discount = $" + str(purchase * 0.2))
else:
    print("Only members are eligible for discounts")