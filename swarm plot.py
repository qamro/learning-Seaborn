import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# swarm plot is an evolution of the strip plot, it avoids overlapping of data points by adjusting their positions.

df = pd.read_csv("students_big_data.csv")

sns.swarmplot(x="Department", y="GPA", data=df,
                hue="Gender", # color the data points based on the department
                dodge=True, # separate the data points for each gender
                size=10, # change the size of the data points
                alpha=0.8) # change the transparency of the data points 

plt.tight_layout()
plt.show()