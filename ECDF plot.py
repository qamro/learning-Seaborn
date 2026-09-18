import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# ECDF(Empirical Cumulative Distribution Function) plot is a way to visualize the distribution of a dataset 
# ECDF plot shows the proportion of data points that are less than or equal to a given value on the x-axis
# and the y-axis shows the cumulative probability of those data points

df = pd.read_csv("students_big_data.csv")