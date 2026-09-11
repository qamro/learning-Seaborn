import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# box plot is used to visualize the distribution of a dataset and to identify outliers  

"""
Box Plot:
Q1 (1st Quartile)  → 25% of the data is below it
Q2 (2nd Quartile)  → Median, 50% of the data is below it
Q3 (3rd Quartile)  → 75% of the data is below it

IQR (Interquartile Range) = Q3 - Q1
The Box represents the middle 50% of the data (Q1 → Q3)
The line inside the Box represents the Median (Q2)
Whiskers extend to the smallest/largest non-outlier values

Outliers are values outside:
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
"""

