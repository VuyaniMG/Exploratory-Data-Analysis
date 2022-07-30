#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# In[2]:

#Load the student enrolments data from the excel file 
Student_df = pd.read_excel("01-student-enrolments.xlsx", header=None, \
                           names = ["University","2009 – Headcounts","2009 - FTEs","2010 – Headcounts","2010 – FTEs","2011 – Headcounts",
                                                              "2011 – FTEs","2012 – Headcounts","2012 – FTEs","2013 – Headcounts","2013 – FTEs"])
#Check the first 5 rows of the data
Student_df.head()


# In[3]:

#Drop the first three rows on the df and reset the index
Student_df.drop(index=Student_df.index[:3], axis = 0, inplace = True)

#Check the first 5 rows of the df
Student_df.head()
# In[4]:

#Reset the index
Student_df.reset_index(drop = True, inplace = True)

#Check the first 5 rows of the df
Student_df.head()
# In[5]:

#Check the first 5 rows of the df
Student_df.tail()

# In[6]:

#Drop the last column
Student_df.drop(Student_df.index[-1:], inplace = True)

#Check the first 5 rows of the df
Student_df.tail()
# In[7]:

#Check the data types
Student_df.dtypes
# In[8]:

#Convert all numeric columns to integer type
Student_df[Student_df.columns[1:]] = Student_df[Student_df.columns[1:]].astype(int)

#Check the data types
Student_df.dtypes
# In[9]:

#Take a look at the summary stats of the dataset
Student_df.describe()
# In[10]:

#Check the info
Student_df.info()
# In[11]:

#This row has a long University name; shorten it
Student_df.University.replace({"UL (Includes Sefako Makgoto Health Sciences University)": "UL+SMU"}, inplace=True)
# In[12]:

#Make bar plots
for feature in Student_df.columns[1:]:
    sns.barplot(x = "University", y = feature, data = Student_df, order = Student_df.sort_values(feature, ascending=False).University)
    plt.title(feature)
    plt.xticks(rotation = 90)
    plt.show()

# %%
