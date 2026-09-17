import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

plt.xticks(np.arange(9, 19, 1)) # set the x-axis ticks to be from 9 to 18 with a step of 1

sns.histplot(x="GPA", data=df,
                hue="Gender", # split the data into groups based on gender
                multiple="stack", # stack the bars for each gender on top of each other
                bins=np.arange(9, 19, 1), # number of bins to divide the data into
                kde=True) # show the kernel density estimation curve on top of the histogram
            
plt.tight_layout()
plt.show()            