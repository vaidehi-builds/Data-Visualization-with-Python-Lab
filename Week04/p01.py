# /*1. Create a Series from a list of integers representing daily 
# temperatures (in Celsius) over a week. Assign index labels as day 
# of the week. 
# a. Find and print the average (mean) temperature for the week. 
# b. Identify and print the maximum and minimum temperatures and their respective days. 
# c. Display the temperatures greater than a specific value. 
# d. Convert all temperatures to Fahrenheit. 
# e. Print the days had temperatures above the average. 
import pandas as pd
temps=pd.Series([25,27,23,26,28,32,31],["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
print("Weekly Temperatures: ")
print(temps)

print("Average Temperatures: ",temps.mean().round(2))
print("Maximum Temperature: ",temps.max(),"on",temps.idxmax())
print("minimum temperature: ",temps.min(),"on",temps.idxmin())

value=30
print("\nTemperature greater than ",value,": ")
print(temps[temps>value])

fhrnt=(temps*9/5)+32
print("Temperatures in fahrenheit: ")
print(fhrnt)

print("Days when temperautre is above the average: ")
print(temps[temps>temps.mean()])