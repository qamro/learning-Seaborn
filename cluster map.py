import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# cluster map is a heatmap with hierarchical clustering of the rows and columns

df = pd.read_csv("students_big_data.csv")

numeric_columns = ['GPA','Assignment_Score','Midterm_Score','Final_Exam_Score','Project_Score',
                    'Study_Hours_Per_Week','Sleep_Hours_Per_Night','Attendance_Percentage',
                    'Stress_Level','Daily_Screen_Time_Hours','Social_Media_Hours',
                    'Satisfaction_Score','Monthly_Expenses_DZD','Height_cm','Weight_kg',
                    'Graduation_Probability_Percentage']


# create a cluster map of the correlation matrix with annotations and a color map
sns.clustermap(df[numeric_columns].corr(), # set the data to be the correlation matrix of the numeric columns in the dataframe
                vmin=-1, # set the minimum value of the color map to be -1
                vmax=1, # set the maximum value of the color map to be 1
                center=0, # set the center of the color map to be 0
                annot=True, # show the correlation values on the cluster map
                fmt=".2f", # set the format of the correlation values to be 2 decimal places
                annot_kws={"size": 10, "weight": "bold"}, # set the size of the annotation text to be 10 and the weight to be bold
                linewidths=0.5, # set the width of the lines between the cells to be 0.5
                linecolor="black", # set the color of the lines between the cells to be black
                cmap="coolwarm") # set the color map for the cluster map

plt.tight_layout()
plt.show()

