import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")
print(df.head()) # show the first 5 rows of the dataset

# create a bar plot to show the average GPA of each department
sns.barplot(x="Department", y="GPA",
            hue="Gender", # split the data into groups based on gender
            data=df,
            ci=None, # remove the confidence interval(the error bars) from the plot
            color="blue") # change the color of the bars to blue

plt.tight_layout()
plt.show()
