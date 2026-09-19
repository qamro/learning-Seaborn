import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# NOTE: Joint plot shows the relationship between two variables along with their distributions. 
"""
joint plot is a combination of scatter plot and histogram or KDE plot by default.
but we can change the kind of the plot to be a regression plot, hexbin plot.... using the kind parameter.
by default, the kind parameter is set to "scatter" which means scatter plot.
like this:
sns.jointplot(x="GPA", y="Study_Hours_Per_Week", data=df,
                kind="reg") # change the kind of the plot to be a regression plot instead of the default scatter plot
"""


                
df = pd.read_csv("students_big_data.csv")

sns.jointplot(x="GPA", y="Study_Hours_Per_Week", data=df,
                joint_kws={"color": "red"}, # change the color of the scatter plot points
                marginal_kws={"color": "green", "kde": True}, # change the color of the histogram bars
                marginal_ticks=True) # show the ticks on the marginal axes

plt.tight_layout()
plt.show()