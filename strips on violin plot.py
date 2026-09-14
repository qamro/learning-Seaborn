import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns  

df = pd.read_csv("students_big_data.csv")

# create a strip plot on top of a violin plot 
sns.stripplot(x="Department", y="GPA", data=df,
                jitter=True, # add some random noise to the data points to avoid overlapping
                linewidth=0.5, # change the width of the data points
                dodge=True, # separate the data points for each gender
                alpha=0.8) # change the transparency of the data points

# create a violin plot on top of the strip plot
sns.violinplot(x="Department", y="GPA", data=df,  
                inner="quartile", # show the quartiles(Q1,median,Q3) inside the violin plot as lines not the default "box" which shows the box plot inside the violin plot
                linewidth=2) # change the width of the violin lines

plt.tight_layout()
plt.show()