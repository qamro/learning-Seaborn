import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# heat map is a graphical representation of data where the individual values contained in a matrix are represented as colors
# it is used to visualize the correlation between different variables in a dataset

df = pd.read_csv("students_big_data.csv")

numeric_columns = ['GPA','Assignment_Score','Midterm_Score','Final_Exam_Score','Project_Score',
                    'Study_Hours_Per_Week','Sleep_Hours_Per_Night','Attendance_Percentage',
                    'Stress_Level','Daily_Screen_Time_Hours','Social_Media_Hours',
                    'Satisfaction_Score','Monthly_Expenses_DZD','Height_cm','Weight_kg',
                    'Graduation_Probability_Percentage']


plt.figure(figsize=(12, 8)) # set the figure size to be 12 inches wide and 8 inches tall

# show the correlation matrix as a heat map with annotations and a color map
sns.heatmap(df[numeric_columns].corr(), # set the data to be the correlation matrix of the numeric columns in the dataframe
            annot=True, # show the correlation values on the heat map
            fmt=".2f", # set the format of the correlation values to be 2 decimal places
            annot_kws={"size": 10, "weight": "bold"}, # set the size of the annotation text to be 10 and the weight to be bold
            linewidths=0.5, # set the width of the lines between the cells to be 0.5
            linecolor="black", # set the color of the lines between the cells to be black
            cmap="coolwarm") # set the color map for the heat map

plt.tight_layout()
plt.show()