import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

sns.histplot(x="GPA", data=df,
                hue="Gender", # split the data into groups based on gender
                multiple="stack", # stack the bars for each gender on top of each other
                bins=10, # number of bins to divide the data into
                element="poly", # change the style of the histogram to polygons instead of filled bars
                kde=True) # show the kernel density estimation curve on top of the histogram
            
plt.tight_layout()
plt.show()            