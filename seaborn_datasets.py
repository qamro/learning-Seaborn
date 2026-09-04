import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# NOTE: seaborn has a lot of built-in datasets that we can use to practice our data visualization skills

# list of all the built-in datasets in seaborn
print(sns.get_dataset_names())
print()

# load the "titanic" dataset from seaborn(for example)
titanic_data = sns.load_dataset("titanic")  
print(titanic_data.head())  # print the first 5 rows of the dataset