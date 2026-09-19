import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

sns.lineplot(x="Study_Hours_Per_Week", y="GPA", data=df,
                hue="Gender", # split the data into groups based on gender
                style="Gender", # change the line style based on gender(make the lines for male and female different)
                palette=["blue", "orange"], # set the colors for the lines based on gender
                markers=True, # show markers on the lines
                dashes=False, # remove the dashed lines from the plot and make the lines solid
                ci=None) # remove the confidence interval from the plot

plt.tight_layout()
plt.show()