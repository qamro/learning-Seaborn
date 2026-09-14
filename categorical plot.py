import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# categorical plot is a type of plot that can create different types of plots based on the type of data.
# It can create bar plots, box plots, violin plots, strip plots, swarm plots, etc.
# NOTE: categorical plot creates strip plots by default, but you can change the type of plot by using the kind parameter.

df = pd.read_csv("students_big_data.csv")

# create a categorical plot that creates two violin plots each one represent a different gender
sns.catplot(x="Department", y="GPA", data=df, 
                col="Gender", # create a separate plot for each gender
                kind="violin", # change the type of plot to violin plot
                inner="quartile", # show the quartiles(Q1,median,Q3) inside the violin plot as lines not the default "box"
                color="lightgray", # change the color of the violin plots
                linewidth=2) # change the width of the violin lines

plt.tight_layout()
plt.show()
