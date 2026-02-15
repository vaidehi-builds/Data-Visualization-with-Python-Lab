# Question 2:
# 1. Load the CEREALS dataset and inspect missing values. 
# 2. Calculate average calories, sugar, and fiber content. 
# 3. Create a bar chart showing top 5 cereals with highest sugar content. 
# 4. Visualize the relationship between calories and rating. 
# 5. Compare cold vs hot cereals based on calorie distribution. 
# 6. Identify healthier cereals using at least two nutritional parameters. 
# 7. Summarize findings using one key visualization and explanation. 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_raw=pd.read_csv("Week06/cereal.csv",)
df=df_raw.copy()

print("First 5 rows: ")
print(df.head())

print("\nDataset Info: ")
df.info()

print("\nNumber of NaN values per column: ")
print(df.isnull().sum())

print("\nNumber of (-1) values in each column: ")
print((df==(-1)).sum())

df['fiber']=df['fiber'].replace(-1,df["fiber"].mean())

print("Average Calories: ",df['calories'].mean().round(2))
print("AVerage sugars: ",df['sugars'].mean().round(2))
print("Average fiber: ",df['fiber'].mean().round(2))

df_sugar=df.sort_values(by='sugars',ascending=False).head()
plt.figure(figsize=(8,6))
x=df_sugar['name']
y=df_sugar['sugars']
plt.bar(x,y,width=0.2,color='blue')
plt.title("Top 5 Cereals with highest Sugar content")
plt.xlabel("Cereals")
plt.ylabel("Sugar Content")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
x=df['calories']
y=df['rating']
plt.scatter(x,y,color='red',alpha=0.7)
plt.title("Relationship between Calories and Rating")
plt.xlabel("Calories")
plt.ylabel("Rating")
plt.grid(True,linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()

print(df['type'].unique())
print(df['type'].value_counts())

cold=df[df['type']=='C']['calories']
hot=df[df['type']=='H']['calories']

plt.figure(figsize=(8,6))
plt.boxplot([cold,hot],tick_labels=["Cold","Hot"])

plt.title("Calorie Distribution for Hot vs Cold Cereals")
plt.ylabel("Calories")
plt.grid(True, linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()

avg_sugar=df['sugars'].mean()
avg_fiber=df['fiber'].mean()
healthy=df[(df['sugars']<=avg_sugar) & (df['fiber']>=avg_fiber)]
print("\nHealthier Cereals based on Sugar and Fiber content: ")
print(healthy[['name','sugars','fiber','calories']])

plt.figure(figsize=(8,6))
plt.scatter(df['sugars'], df['fiber'], alpha=0.6)
plt.axvline(avg_sugar, color='red', linestyle='--', label='Average Sugar')
plt.axhline(avg_fiber, color='blue', linestyle='--', label='Average Fiber')
plt.title("Healthy Cereal Region (Low Sugar, High Fiber)")
plt.xlabel("Sugar")
plt.ylabel("Fiber")
plt.legend()
plt.tight_layout()
plt.show()


print("The cereals dataset reveals significant variation in nutritional quality across products.")
print("The scatter plot shows a moderate negative relationship between calories and rating, indicating that lower-calorie cereals tend to receive higher ratings.")
print("Cold cereals exhibit greater variability in calorie and sugar content compared to hot cereals.")
print("A subset of cereals with low sugar and high fiber emerges as healthier options, highlighting the importance of balanced nutritional design.")





                


