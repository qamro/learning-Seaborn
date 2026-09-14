import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

# create a strip plot on top of a box plot 
sns.stripplot(x="Department", y="GPA", data=df,
                jitter=True, # add some random noise to the data points to avoid overlapping
                linewidth=0.5, # change the width of the data points
                alpha=0.8) # change the transparency of the data points

# create a box plot on top of the strip plot
sns.boxplot(x="Department", y="GPA", data=df,  
            showmeans=True, # show the mean of the data as a point on the box plot
            meanprops={"marker":"D", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":8},#customize the mean point
            linewidth=2) # change the width of the box lines

plt.tight_layout()
plt.show()