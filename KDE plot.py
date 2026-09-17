import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

sns.kdeplot(x="GPA", data=df,
                hue="Gender", # split the data into groups based on gender
                multiple="stack", # stack the density curves for each gender on top of each other and fill the area under the curves
                linewidth=2, # set the width of the density curves
                alpha=0.5) # set the transparency of the density curves

plt.tight_layout()
plt.show()