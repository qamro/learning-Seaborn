import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns  

df = pd.read_csv("students_big_data.csv")

# create a swarm plot on top of a violin plot
sns.swarmplot(x="Department", y="GPA", data=df,
                color="green", # change the color of the data points
                size=10, # change the size of the data points
                alpha=0.8) # change the transparency of the data points 

# create a violin plot on top of the swarm plot
sns.violinplot(x="Department", y="GPA", data=df,
                inner="quartile", # show the quartiles(Q1,median,Q3) inside the violin plot as lines not the default "box" which shows the box plot inside the violin plot
                color="lightgray", # change the color of the violin plots
                linewidth=2) # change the width of the violin lines

plt.tight_layout()
plt.show()