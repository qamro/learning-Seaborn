import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# rug plot shows the distribution of a single variable by drawing a small vertical line at each observation's position on the x-axis

df = pd.read_csv("students_big_data.csv")

# create a rug plot to show the distribution of GPA with a histogram and a kernel density estimation curve

sns.histplot(x="GPA", data=df,
                bins=np.arange(9, 19, 1), # number of bins to divide the data into
                kde=True) # show the kernel density estimation curve on top of the histogram

sns.rugplot(data=df, x="GPA", color="black", height=0.05)


plt.tight_layout()
plt.show()