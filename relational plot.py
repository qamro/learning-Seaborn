import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# relational plot is used to create scatter plots and line plots to visualize the relationship between two variables
# relational plot creates scatter plots by default but we can change it to line plots by setting the kind parameter to "line"

df = pd.read_csv("students_big_data.csv")

sns.relplot(x="Study_Hours_Per_Week", y="GPA", data=df,
            col="Department", # create a separate plot for each department
            col_wrap=3, # wrap the plots into 3 columns(distribute the plots into 3 columns)
            hue="Gender", # split the data into groups based on gender
            style="Gender", # change the points style based on gender(make the points for male and female different)
            s=70, # set the size of the scatter plot points
            palette=["blue", "orange"]) # set the colors for the markers based on gender)

plt.tight_layout()
plt.show()