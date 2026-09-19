import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# FacetGrid is a way to create multiple plots 
# It allows us to create a grid of subplots

df = pd.read_csv("students_big_data.csv")

# create a FacetGrid with columns based on Department and rows based on Gender
grid = sns.FacetGrid(df, col="Department", row="Gender",
                    sharex=False, # allow each subplot to have its own x-axis scale
                    sharey=False) # allow each subplot to have its own y-axis scale

grid.map_dataframe(sns.histplot, x="GPA", bins=10, kde=True) # create a histogram for each gender and department combination
grid.set_axis_labels("GPA", "Count") # set the x(GPA) and y(Count) axis labels
grid.set_titles(col_template="{col_name}", row_template="{row_name}") # set the titles for each subplot based on the column and row names

plt.tight_layout()
plt.show()