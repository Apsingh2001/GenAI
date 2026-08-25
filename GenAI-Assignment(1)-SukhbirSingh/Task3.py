# Product Pricing (Dictionaries)

'''reate a dictionary price_dict where keys are product names and values are prices
(integers or floats). Include at least 6 entries'''

price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Tablet": 399.99,
    "Headphones": 199.99,
    "Smartwatch": 299.99,
    "Camera": 599.99
}

'''Write small code blocks to:
Add a new product with price to price_dict.
- Update the price of an existing product.
- Remove a product by name (handle the case when the product does not exist)'''

# Add a new product with price to price_dict
price_dict["Gaming Console"] = 499.99

# Update the price of an existing product
price_dict["Laptop"] = 899.99

# Remove a product by name (handle the case when the product does not exist)
if "Tablet" in price_dict:
    del price_dict["Tablet"]
else:
    print("Product not found.")

# Print the average price of all products
average_price = sum(price_dict.values()) / len(price_dict)
print("Average price of all products:", average_price)

# Print the product with the maximum price
max_product = max(price_dict, key=price_dict.get)
print("Product with the maximum price:", max_product, "-", price_dict[max_product])

# Print the product with the minimum price
min_product = min(price_dict, key=price_dict.get)
print("Product with the minimum price:", min_product, "-", price_dict[min_product])

'''Print the average price of all products (use only dictionary 
operations and basic arithmetic)'''
average_price = sum(price_dict.values()) / len(price_dict)
print("Average price of all products:", average_price)

'''Print the product with both the maximum and minimum prices.'''
print("Product with the maximum price:", max_product, "-", price_dict[max_product])
print("Product with the minimum price:", min_product, "-", price_dict[min_product])