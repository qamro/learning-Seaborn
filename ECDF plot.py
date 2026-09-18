import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# ECDF(Empirical Cumulative Distribution Function) plot is a way to visualize the distribution of a dataset 
# ECDF plot shows the proportion(percentile) of data points that are less than or equal to a given value on the x-axis
# and the y-axis shows the cumulative probability of those data points

df = pd.read_csv("students_big_data.csv")

# create an ECDF plot to show the distribution of GPA 
sns.ecdfplot(x="GPA", data=df,
            hue="Gender") # split the data into groups based on gender

plt.tight_layout()
plt.show()


"""
ECDF plot is showing the proportion by default.
but we can change it to show the count of data points by using the stat parameter and setting it to "count.
like this:
sns.ecdfplot(x="GPA", data=df,
            hue="Gender", # split the data into groups based on gender
            stat="count") # show the count of data points instead of proportion
"""