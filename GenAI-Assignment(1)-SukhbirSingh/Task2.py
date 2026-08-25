# Categories (Sets)
# From your products list, create a set of categories called categories_set. (If product names do not contain categories, create a short parallel list categories = [ .. ] with matching length and use that.)

categories = ["Electronics", "Fruits", "Electronics", "Furniture", "Dairy", "Books"]
categories_set = set(categories)
print("Unique Categories:", categories_set)

# Demonstrate adding a new category to the set and show that duplicates are ignored.

categories_set.add("Books") # Adding a duplicate category
print("Categories after adding a duplicate:", categories_set)

# Show how to check whether a category exists in the set (print a boolean result).
print("Does 'Electronics' exist in the set?", "Electronics" in categories_set)

# Show how to get the total number of unique categories using a set.
print("Total unique categories:", len(categories_set))