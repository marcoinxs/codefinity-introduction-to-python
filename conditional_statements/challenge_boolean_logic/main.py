seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

overstock_risk = seasonal and (current_stock > high_stock_threshold)

seasonal = False
current_stock = 200
discount_eligible = not selling_well and not on_sale

make_discount = overstock_risk or discount_eligible

#print(overstock_risk)
print(discount_eligible)

print(f" Should the item be discounted? {make_discount}.")