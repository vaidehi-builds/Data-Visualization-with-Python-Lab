"""5. Write a Python function that takes a string input from the user 
and counts the number of vowels and consonants in the string. """
def count(text):
    vc=0
    cc=0
    for ch in text:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vc+=1
            else:
                cc+=1
    print("Vowels: ",vc)
    print("Consonants: ",cc)

istring=input("Enter a string: ")
count(istring)