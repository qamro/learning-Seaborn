import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

"""
NOTE: 
KDE (Kernel Density Estimation) estimates the density/distribution of the data.
In a violin plot, the width of the violin represents the density of data at that value:
wider = higher density (more data concentrated around that value)
narrower = lower density (less data around that value)
KDE creates the smooth shape of the violin plot.
"""

sns.violinplot(x="Department", y="GPA", data=df,
                hue="Gender", # split the data into groups based on gender
                split=True, # split the violins into two halves for each gender
                inner="quartile", # show the quartiles(Q1,median,Q3) inside the violin plot as lines not the default "box" which shows the box plot inside the violin plot
                linewidth=2) # change the width of the violin lines

plt.tight_layout()
plt.show()