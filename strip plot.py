import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

sns.stripplot(x="Department", y="GPA", data=df,
                hue="Gender", # split the data into groups based on gender
                jitter=True, # add some random dispersion to the data points to avoid overlapping 
                linewidth=0.5, # change the width of the data points
                dodge=True, # separate the data points for each gender
                alpha=0.8) # change the transparency of the data points

plt.tight_layout()
plt.show()

"""
NOTE:
u can control the jittering of the data points using the jitter parameter:
jitter=True → add some random dispersion to the data points to avoid overlapping and see the distribution of the data points 
jitter=False → no random dispersion, the data points will be plotted on top of each other if they have the same value
jitter=0.3 → add a precise amount of random dispersion to the data points 
"""

"""
NOTE:
u can control the size of the data points using the size parameter for example:
size=5
"""