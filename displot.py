import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# Displot (Distribution plot) is a combination of histogram and KDE plot and rug plot.

df = pd.read_csv("students_big_data.csv")

sns.displot(x="GPA", data=df,
            col="Gender", # create separate plots for each gender
            bins=np.arange(9, 19, 1), # number of bins to divide the data into
            kde=True, # show the kernel density estimation curve on top of the histogram
            rug=True) # show the rug plot on the x-axis to indicate the individual data points

plt.tight_layout()
plt.show()