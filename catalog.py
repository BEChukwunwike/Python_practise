def cal_total_price(item1= None, item2= None, item3= None):
    # Calculates the total price based on the items purchased.

    # If only one item is purchased
    if item1 is not None and item2 is None and item3 is None:
        purchase = item1

    # If two items are purchased
    elif item1 is not None and item2 is not None and item3 is None:
        purchase = item1 + item2

    # If three items are purchased
    else:
        purchase = item1 + item2 + item3

     # Apply discounts
    if (item1 == item2 == item3) or (item2 == None and item3 == None):
        # individual items
        total_price = purchase

    elif (item1 != item2) and (item3 == None or item3 == item1 or item3 == item2):
        # combo pack with two unique items
        total_price = purchase - (purchase * 0.10)

    else:
        # gift pack with three unique items
        total_price = purchase - (purchase * 0.25)

    return(total_price)


print(
    "Online Store\n---------------------\nProducts(S)                    Price\nItem 1                         "+
    str(cal_total_price(200.0))+ "\nItem 2                         " + str(cal_total_price(400.0)) +
    "\nItem 3                         " + str(cal_total_price(600.0)) +
    "\nCombo 1(Item 1 + 2)            " + str(cal_total_price(200,400)) +
    "\nCombo 2(Item 2 + 3)            " + str(cal_total_price(400,600)) +
    "\nCombo 3(Item 1 + 3)            " + str(cal_total_price(200,600)) +
    "\nCombo 4(Item 1 + 2 + 3)        " + str(cal_total_price(200,400,600)) +
    "\n_________________________\nFor delivery Contact:98764678899"
    )