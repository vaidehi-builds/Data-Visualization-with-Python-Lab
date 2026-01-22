"""1. Write a Python code block that inputs numbers into a list. Print 
the largest, smallest, the sum, and the average of the numbers. 
Count occurrences of a specific number in the list. """
num=[] 
n=int(input("How many numbers? "))
for i in range(n):
    num.append(int(input("Enter number: ")))
print("Largest: ",max(num))
print("Smallest: ",min(num))
print("Sum: ",sum(num))
print("Average: ",sum(num)/len(num))
find=int(input("Enter the number to be searched: "))
print("Occurences: ",num.count(find))