# 2. For the CEREALS dataset, perform data preprocessing and  answer the following questions. 
# a. Create a table with the 5 number summary of all the numeric  attributes. 
# b. For each of the numeric attributes (proteins upto vitamins), identify and replace all missing data(indicated with -1) with  the arithmetic mean of the attribute. 
# c. Create a table with the 5 number summary of all the numeric attributes after treating missing values. 
# Do you think the  strategy used in dealing with missing values was effective? 
# d. For each numeric attribute (proteins upto vitamins), identify  and replace all noisy data with the median of attribute. 
# e. Create a table with the 5 number summary of all the numeric attributes after treating noisy values. 
# Do you think the strategy used in dealing with noisy values was effective? 

import pandas as pd
import numpy as np

cereal_df=pd.read_csv("Week05/cereal.csv")

numeric_col=cereal_df.select_dtypes(include=np.number)
def five_number(data):
    return data.describe().loc[["min","25%","50%","75%","max"]]

print("5 Number Summary (Before Cleaning): ")
print(five_number(numeric_col))

cereal_clean=cereal_df.copy()
nutrient_cols=cereal_clean.loc[:,"protein":"vitamins"].columns
for col in nutrient_cols:
    cereal_clean[col]=cereal_clean[col].replace(-1,np.nan)
    cereal_clean[col] = cereal_clean[col].fillna(cereal_clean[col].mean())

print("\n")
print("5 NUmber Summary after Missing treatment: ")
print(five_number(cereal_clean[nutrient_cols]))
print("After replacing the missing values (-1) with the arithmetic mean, the minimum values increased to valid ranges, indicating successful handling of missing data.") 
print("The quartiles and median values did not change significantly, which suggests that mean imputation did not distort the overall distribution of the dataset. ") 
print("Therefore, the strategy was effective in correcting missing values while preserving the structure of the data.")

for col in nutrient_cols:
    Q1=cereal_clean[col].quantile(0.25)
    Q3=cereal_clean[col].quantile(0.75)
    IQR=Q3-Q1

    lower=Q1-1.5*IQR
    upper=Q3+1.5*IQR
    median=cereal_clean[col].median()
    cereal_clean[col]=np.where((cereal_clean[col] < lower) | (cereal_clean[col] > upper), median,cereal_clean[col])

print("\n")
print("5 number summary after Noisy Treatment: ")
print(five_number(cereal_clean[nutrient_cols]))
print("After applying the IQR method and replacing outliers with the median, extreme maximum values reduced significantly, and the range of the data decreased. " )
print("This indicates that statistical outliers were successfully identified and adjusted. The distribution became less skewed and more compact. " )
print("Hence, the strategy was effective in reducing the impact of extreme values. However, some high values such as protein levels may represent valid extreme cases," )
print("so domain knowledge should be considered before finalizing such transformations.")