import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

data = pd.read_csv("students.csv")
# add new column to our data
data["Gender"] = ["M", "M", "F", "F", "M"]
print(data)

# customize the size of the figure
plt.figure(figsize=(15, 5))

# create a count plot that counts the number of the gender 
sns.countplot(x="Gender", data=data)

plt.show()

"""
here how to customize the count plot to be with two variables:
sns.countplot(x="Country", hue="Gender", data=data)
NOTE: hue is used to split your data into groups and give each group a different color 
NOTE: when we used hue the legend will be shown automatically
"""