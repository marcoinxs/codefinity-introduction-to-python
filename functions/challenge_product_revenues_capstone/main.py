# You must define the following functions:
# calculate_revenue(prices, quantities_sold): This function should multiply each price by its corresponding quantity sold, store the results in a list, and return this list of revenues.
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        total_revenue = prices[i] * quantities_sold[i]
        revenue.append(total_revenue)
    return revenue

# formatted_output(revenues): This function should take a list of (product_name, revenue) tuples, sort them alphabetically by product name, and print each in the specified format.
def formatted_output(revenues):
    revenues.sort(key=lambda x: x[0])
    for product, revenue in revenues:
        print(f"{product} has total revenue of ${revenue}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")

# Calculate the revenue for each product by multiplying the price by the quantity sold, and store all results in a new list called revenue;
revenue = []
for i in range(len(products)):
    total_revenue = prices[i] * quantities_sold[i]
    revenue.append((products[i], total_revenue))
    
# Use the zip() function to combine the products and revenue lists into a list of tuples named revenue_per_product, where each tuple contains a product name and its corresponding revenue;
revenue_per_product = list(zip(products, revenue))
#Sort the revenue_per_product list alphabetically by product name;
revenue_per_product.sort(key=lambda x: x[0])

#Print each product and its revenue using this format: <product_name> has total revenue of $<revenue>.
for product, revenue in revenue_per_product:
    print(f"{product} has total revenue of ${revenue[1]}")  

# After defining these functions, use the provided lists to call them and display the results as described above.
# Calculate the revenue for each product
revenues = calculate_revenue(prices, quantities_sold)
# Combine products with their revenues into a list of tuples
#revenue_per_product = list(zip(products, revenues))
revenue_per_product = sorted(zip(products, revenues))
# Print the formatted output
formatted_output(revenue_per_product)

