import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")
print(df.head()) # show the first 5 rows of the dataset

# create a bar plot to show the average GPA of each department
sns.barplot(x="Department", y="GPA", data=df) 

plt.tight_layout()
plt.show()