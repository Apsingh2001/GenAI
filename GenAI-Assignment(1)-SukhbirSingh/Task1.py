# Product Collections (Lists & Tuples)

# Create a list named products containing at least 6 product names (Strings).
products = ["Laptop", "Apple", "Smartphone", "Desk", "Milk","Books"]

#Create a tuple named sample_Products that stores (product_name, price, Category) for one product.
sample_Products = ("Laptop", 1200.00, "Electronics")

#Print the 2nd and last product from the products list.
print("2nd Product:", products[1])
print("Last Product:", products[-1])

#Append two new product names to products and then print the updated list.
products.append("Headphones")
products.append("Microphone")
print("Updated Products List:", products)

#Convert sample_product into a list, change its price, and convert it back to a tuple.
sample_Products_list = list(sample_Products)
sample_Products_list[1] = 1100.00  # Change price
sample_Products = tuple(sample_Products_list)