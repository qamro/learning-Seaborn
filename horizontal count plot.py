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
sns.countplot(y="Gender", data=data)

plt.show()