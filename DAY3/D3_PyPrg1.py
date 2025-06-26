# ---New code for Set Operation and List De-duplication ---

print("---Set Operation---")

# Create teo sets
set_a = {10, 20, 30, 40, 50, 50,40}
set_b = {40, 50, 60, 70, 80, 90, 100}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Find the uniuon of set_a and set_b and print the result:
# The union contains all unique elements from both sets.

union_set = set_a.union(set_b)
print(f"Union of Set A and Set B: {union_set}")


intersection_set = set_a.intersection(set_b)
print(f"Intersection of Set A and Set B: {intersection_set}")

differencen_set = set_a.difference(set_b)
print(f"Difference of Set A and Set B: {differencen_set}")

# Create a list with duplicates
my_list =[1, 2, 2, 3, 4, 4, 5, 1, 6]
print(f"List : {my_list}")

# Convert my list to a set to remove duplicates.
# Sets inherently store only unique elements. 
unique_element_set = set(my_list)
print(f"List converted to set (duplicate removed): {unique_element_set}")

# Covert the set back to a list.
# The order of elements might not be preserved from the original liat

unique_list = list(unique_element_set)
print(f"Converted set back list: {unique_list}")