import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# regression plot is a scatter plot with a regression line fitted to the data points

df = pd.read_csv("students_big_data.csv")

sns.regplot(x="Study_Hours_Per_Week", y="GPA", data=df,
            line_kws={"color": "red", "linestyle": "--"}, # change the color and linestyle of the regression line
            scatter_kws={"color": "green", "s": 80, "alpha": 0.5}) # change the color, size and transparency of the scatter plot points

plt.tight_layout()
plt.show()