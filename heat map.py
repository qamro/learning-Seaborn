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

