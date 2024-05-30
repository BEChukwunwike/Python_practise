cover_price =  24.95
discount = 0.4
shipping_cost = 3
additional_shipping_cost = 0.75
no_of_copies = 60
discount_per_book = cover_price * discount
wholesale_per_book = cover_price - discount_per_book
number_of_additional_cost = no_of_copies - 1
total_additional_shipping_cost = additional_shipping_cost + number_of_additional_cost
total_wholesale_cost = (wholesale_per_book * no_of_copies) + shipping_cost + total_additional_shipping_cost
print(total_wholesale_cost)