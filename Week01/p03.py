"""3. Create a Python function that creates a sequence between 1 and
100 and prints all the odd numbers. Compute and display the sum 
of all the even numbers."""

def printseq():
    evensum=0
    for i in range(1,100+1):
        if i%2!=0:
            print(i, end=" ")
        else:
            evensum+=i
    print("\nSum of the even numbers: ",evensum)

printseq()