# Question 1:  For the MTCARS dataset, answer the specified questions with summarization and effective visuals. 
# 1. Load the MTCARS dataset and display its basic structure (rows, columns, data types). 
# 2. Compute summary statistics (mean, median, min, max) for: 
# • Miles per gallon (mpg) 
# • Horsepower (hp) 
# • Weight (wt) 
# 3. Identify the relationship between engine cylinders (cyl) and fuel efficiency (mpg) using  an appropriate visualization. 
# 4. Create a scatter plot between horsepower (hp) and mpg. 
# • Add labels and a meaningful title. 
# 5. Compare manual vs automatic transmission cars in terms of mpg using a box plot. 
# 6. Identify which car model gives the best balance of power and fuel efficiency. Justify  using a visualization. 
# 7. Write a short data story (3–4 lines) summarizing insights derived from the plots.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("Week06/mtcars.csv",index_col=0)
print("First 5 rows: ")
print(df.head())

print("\nShape of the dataset: ")
print(df.shape)

print("\nColumn names: ")
print(df.columns)

print("\nData Types: ")
print(df.dtypes)

print("\nDataset Info: ")
df.info()

summary=df[["mpg", "hp", "wt"]].agg(["mean", "median", "min", "max"])
print("Summary Statistics for mpg, hp and wt: ")
print(summary.round(2))

plt.figure(figsize=(8,6))
plt.boxplot([df[df['cyl']==c]['mpg'] for c in sorted(df['cyl'].unique())],
            tick_labels=[f"{c} Cyl" for c in sorted(df['cyl'].unique())]) # this returns a pandas Series which is then accepted by boxplot() 
plt.show()
print("The boxplot clearly demonstrates an inverse relationship between engine cylinders and fuel efficiency.")
print("Four-cylinder cars have the highest median mpg and greatest variability, while eight-cylinder cars show significantly lower fuel efficiency, with at least one extreme low outlier.")


plt.scatter(df['hp'],df['mpg'],alpha=0.7)
plt.title("Relationship between Horsepower and Fuel Efficiency")
plt.xlabel("Horsepower (hp)")
plt.ylabel("Miles per Gallon (mpg)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
print("The scatter plot shows a clear negative relationship between horsepower and mpg.")
print("Vehicles with higher horsepower tend to have lower fuel efficiency. ")
print("This aligns with engineering principles, as more powerful engines consume more fuel.")

plt.figure(figsize=(8,6))
auto_mpg = df[df['am'] == 0]['mpg']
manual_mpg = df[df['am'] == 1]['mpg']
plt.boxplot([auto_mpg, manual_mpg],
            tick_labels=["Automatic", "Manual"])
plt.title("Fuel Efficiency: Manual vs Automatic Cars")
plt.xlabel("Transmission Type")
plt.ylabel("Miles per Gallon (mpg)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

avg_hp = df['hp'].mean()
avg_mpg = df['mpg'].mean()

balanced_cars = df[
    (df['hp'] >= avg_hp * 0.7) &
    (df['mpg'] >= avg_mpg)
]

print("\nBalanced Cars:")
print(balanced_cars[['hp', 'mpg']])

plt.figure(figsize=(8,6))
plt.scatter(df['hp'], df['mpg'], alpha=0.6)

plt.axhline(avg_mpg, color='red', linestyle='--', label='Average MPG')
plt.axvline(avg_hp, color='blue', linestyle='--', label='Average HP')

plt.title("Balanced Cars: Horsepower vs MPG")
plt.xlabel("Horsepower (hp)")
plt.ylabel("Miles per Gallon (mpg)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

print("While horsepower and fuel efficiency exhibit a clear negative relationship, a small group of vehicles achieve an effective compromise.")
print("Cars with moderate horsepower levels and above-average mpg values demonstrate balanced engineering design.")
print("The Lotus Europa exemplifies this equilibrium between efficiency and capability.")

