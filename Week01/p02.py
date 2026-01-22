"""2. Write a Python function that takes an integer and returns True if it’s a prime number and False otherwise."""
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num=int(input("Enter a number: "))
print(isPrime(num))