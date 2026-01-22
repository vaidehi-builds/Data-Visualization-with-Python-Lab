"""5. Write a Python code block to input numbers into two sets. 
Perform union, intersection, and difference operations on the sets 
and print the results. """

set1=set(input("Enter elements of first set: ").split())
set2=set(input("Enter elements of second set: ").split())
print("Union: ",set1.union(set2))
print("Intersection: ",set1.intersection(set2))
print("Difference: ",set1.difference(set2))

