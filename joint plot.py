import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# joint plot is a combination of scatter plot and histogram by default
# but we can change the kind of the plot to be a regression plot, hexbin plot, or kde plot

# NOTE: It shows the relationship between two variables along with their distributions. 


df = pd.read_csv("students_big_data.csv")

