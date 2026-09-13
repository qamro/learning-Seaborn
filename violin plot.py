import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")

"""
NOTE: 
KDE (Kernel Density Estimation) estimates the density/distribution of the data.
In a violin plot, the width of the violin represents the density of observations:
wider = higher density (more data concentrated around that value)
narrower = lower density (less data around that value)
KDE creates the smooth shape of the violin plot.
"""
