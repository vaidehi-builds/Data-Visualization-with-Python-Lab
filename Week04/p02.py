# 2. Create a data frame with details of 10 students and columns as 
# Roll Number, Name, Gender, Marks1, Marks2, Marks3. 
# a. Create a new column with total marks 
# b. Find the lowest marks in Marks1 
# c. Find the Highest marks in Marks2 
# d. Find the average marks in Marks3 
# e. Find student name with highest average 
# f. Find how many students failed in Marks2 (<40) 
import pandas as pd
data={"Roll Number":[1,2,3,4,5,6,7,8,9,10],
        "Name":["Athreya","Bhumi","Chandani","Dev","Eraya","Freya","Girish","Hansika","Ishaan","Jayant"],
        "Gender":['M','F','F','M','F','F','M','F','M','M'],
        "Marks1":[44,45,41,48,34,65,46,21,40,46],
        "Marks2":[46,21,44,27,48,78,39,47,79,55],
        "Marks3":[75,67,58,46,53,74,55,80,58,46]
}
df=pd.DataFrame(data)
print("Your Data:")
print(df)

df["Total Marks"]=df["Marks1"]+df["Marks2"]+df["Marks3"]
print(df)

print("Lowest marks in subject 1: ",df["Marks1"].min())
print("Highest marks in subject 2: ",df["Marks2"].max())
print("Average marks in subject 3: ",df["Marks3"].mean())
df["Average Marks"]=df[["Marks1","Marks2","Marks3"]].mean(axis=1)
print("Student with highest average: ",df.loc[df["Average Marks"].idxmax(),"Name"])
print("Students failed in subject 2 : ",((df["Marks2"]<40).sum()))
