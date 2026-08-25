import Task1
import Task2
import Task3

# Combined Operations
'''Using the products list and price_dict, create a list of tuples named catalog where
each tuple is (product_name, price, category)'''
product_categories = dict(zip(Task1.products, Task2.categories))
catalog = [
    (product, Task3.price_dict[product], product_categories.get(product, "Other"))
    for product in Task1.products
    if product in Task3.price_dict
]

'''From catalog, create a new dictionary category_to_products that maps each category
to a list of product names in that category'''
category_to_products = {}
for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)
    

# Print the catalog and category_to_products dictionary
print("Catalog:", catalog) 
print("Category to Products:", category_to_products)

'''Print all products that belong to the category that has the maximum number of
Products'''
max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))
print("Products in the category with the most items:", category_to_products[max_category])