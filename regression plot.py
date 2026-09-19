import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# regression plot is a scatter plot with a regression line fitted to the data points

df = pd.read_csv("students_big_data.csv")

sns.regplot(x="Study_Hours_Per_Week", y="GPA", data=df,