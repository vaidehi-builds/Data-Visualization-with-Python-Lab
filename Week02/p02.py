"""2. Write a Python code block to create a tuple with five elements. 
Try to change one of the elements and handle the error that 
occurs. Print a message that explains why the error occurred. """
def check():
    chktup=("Mit",67,True,78,"how")
    chktup+=input("Enter a string: ")
    print(chktup)

check()
print("Error occurs because a tuple can only be concatenated with another tuple.")
print("input() returns a string and tuples are immutable.")
