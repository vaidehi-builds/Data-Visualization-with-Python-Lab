"""4. Write a Python function to add two elements and display the 
result. The elements can be of type integer, float or string. """
def addElements(a,b):
    return(a+b)

print("Choose ethe type of elements to be added:")
print("1.Integer")
print("2.FLoat")
print("3.String")

ch=int(input("Enter your choice: "))

if ch==1:
    
    x=int(input("Enter the first integer: "))
    y=int(input("Enter the second integer: ")) 
    ans=addElements(x,y)
    print("Result: ",ans)

elif ch==2:
    x=float(input("Enter the first float: "))
    y=float(input("Enter the second float: ")) 
    ans=addElements(x,y)
    print("Result: ",ans)

elif ch==3:
    x=input("Enter the first string: ")
    y=input("Enter the second string: ")
    ans=addElements(x,y)
    print("Result: ",ans)

else:
    print("Invalid choice")