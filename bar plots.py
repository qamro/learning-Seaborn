import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

df = pd.read_csv("students_big_data.csv")
print(df.head()) # show the first 5 rows of the dataset

# create a bar plot to show the average GPA of each department
sns.barplot(x="Department", y="GPA",
            hue="Gender", # split the data into groups based on gender
            data=df,
            order=["Computer Science", "Physics", "Mathematics", "Biology", "Business"], # order the departments in a specific order
            hue_order=["Male", "Female"], # order the hue(genders) in a specific order
            ci=None, # remove the confidence interval(the error bars) from the plot
            color="blue", # change the color of the bars to blue
            saturation=0.5) # change the saturation(intensity) of the colors

plt.tight_layout()
plt.show()

"""
NOTE: the default aggregation function for bar plot is mean.
but we can change it to any other aggregation function using the estimator parameter.
for example, if we want to show the sum of the GPA instead of the mean we can use the following code:
sns.barplot(x="Department", y="GPA",
            hue="Gender", # split the data  into groups based on gender
            data=df,
            estimator=sum, # change the aggregation function to sum
            order=["Computer Science", "Physics", "Mathematics", "Biology", "Business"], # order the departments in a specific order
            hue_order=["Male", "Female"], # order the hue(genders) in a specific order
            ci=None, # remove the confidence interval(the error bars) from the plot
            color="blue", # change the color of the bars to blue
            saturation=0.5) # change the saturation(intensity) of the colors    
"""
