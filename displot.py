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
            rug=True, # show the rug plot on the x-axis to indicate the individual data points
            rug_kws={"height": 0.1}) # set the color and height of the rug lines

plt.tight_layout()
plt.show()

"""
NOTE: u can specify the plot type in displot using kind parameter.
The default value of kind is hist which means histogram.
u can create ecdf (Empirical Cumulative Distribution Function) plot using kind="ecdf" and KDE plot using kind="kde".
and u can also create a rug plot using kind="rug".
"""