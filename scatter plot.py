import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

sns.scatterplot(x="Study_Hours_Per_Week", y="GPA", data=df,
                hue="Gender", # split the data into groups based on gender
                style="Gender", # change the marker style based on gender(make the markers for male and female different)
                s=100, # set the size of the markers
                alpha=0.7) # set the transparency of the markers


plt.tight_layout()
plt.show()