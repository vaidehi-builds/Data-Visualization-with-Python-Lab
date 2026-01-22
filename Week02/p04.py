"""4. Write a Python code block that inputs a sentence from the user. 
Count the frequency of each word in the sentence and store the 
result in a dictionary. Prints the dictionary with words as keys 
and their frequencies as values. """

sentence=input("Enter a sentence: ")
words=sentence.split()
freq={}
for word in words:
    freq[word]=freq.get(word,0)+1
print(freq)

