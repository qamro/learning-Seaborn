import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# pair plot is a great way to visualize the relationship between multiple variables in a dataset
# it creates a grid of scatter plots(non diagonal) and histogram(diagonal) by default for each pair of variables in the dataset

df = pd.read_csv("students_big_data.csv")

sns.pairplot(data=df,
            x_vars=["GPA", "Study_Hours_Per_Week", "Sleep_Hours_Per_Night", "Stress_Level", "Attendance_Percentage"], # select the variables to be plotted on the x-axis
            y_vars=["GPA", "Study_Hours_Per_Week", "Sleep_Hours_Per_Night", "Stress_Level", "Attendance_Percentage"], # select the variables to be plotted on the y-axis
            kind="scatter", # set the type of plot(non-diagonal plots) to be scatter plot(its the default one btw)
            plot_kws={"color": "red"}, # set the color of the scatter plot points(non-diagonal plots)
            diag_kind="hist",# set the type of plot to be histogram for the diagonal plots(its the default one btw)
            diag_kws={"color": "green", "kde": True}) # set the color of the histogram bars(diagonal plots)

plt.tight_layout()
plt.show()

"""
NOTE:
u can change the kind of the plots(diagonal and non-diagonal) to be different types of plots like:
any type of the plots in the seaborn library by changing the kind parameter for the non-diagonal plots 
and the diag_kind parameter for the diagonal plots.
"""