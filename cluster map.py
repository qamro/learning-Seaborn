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


plt.figure(figsize=(12, 8)) # set the figure size to be 12 inches wide and 8 inches tall
