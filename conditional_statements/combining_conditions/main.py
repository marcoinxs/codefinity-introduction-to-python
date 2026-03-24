# The item's discount and stock status have been defined
discounted = True
lowStock = not True
movingProduct = (discounted == True) or (lowStock == True) 
promotion = (discounted == False) or (lowStock == True)

#print(f"Is the item have Discount or is Low Stock? {movingProduct}")
print(f"Is the item eligible for promotion? {promotion}")
