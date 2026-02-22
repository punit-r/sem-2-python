#Write a program to demonstrate the setfunctions and operations. 


# Create two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Set1 =", set1)
print("Set2 =", set2)

# 1. add() function
set1.add(100)
print("\nAfter add(100) in Set1 =", set1)

# 2. remove() function
set1.remove(20)
print("After remove(20) from Set1 =", set1)

# 3. union() operation
print("\nUnion of Set1 and Set2 =", set1.union(set2))

# 4. intersection() operation
print("Intersection of Set1 and Set2 =", set1.intersection(set2))

# 5. difference() operation
print("Difference (Set1 - Set2) =", set1.difference(set2))

# 6. symmetric_difference() operation
print("Symmetric Difference =", set1.symmetric_difference(set2))

# 7. issubset() function
print("\nIs Set1 subset of Set2? =", set1.issubset(set2))

# 8. issuperset() function
print("Is Set1 superset of Set2? =", set1.issuperset(set2))

# 9. clear() function
set2.clear()
print("\nAfter clear() Set2 =", set2)