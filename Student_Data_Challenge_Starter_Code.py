#!/usr/bin/env python
# coding: utf-8

# ### Import required dependencies

# In[18]:


import pandas as pd
import os


# ## Deliverable 1: Collect the Data
# 
# To collect the data that you’ll need, complete the following steps:
# 
# 1. Using the Pandas `read_csv` function and the `os` module, import the data from the `new_full_student_data.csv` file, and create a DataFrame called student_df. 
# 
# 2. Use the head function to confirm that Pandas properly imported the data.
# 

# In[19]:


# Create the path and import the data
full_student_data = os.path.join('new_full_student_data.csv')
student_df = pd.read_csv(full_student_data)


# In[20]:


# Verify that the data was properly imported
student_df.head()


# ## Deliverable 2: Prepare the Data
# 
# To prepare and clean your data for analysis, complete the following steps:
#     
# 1. Check for and remove all rows with `NaN`, or missing, values in the student DataFrame. 
# 
# 2. Check for and remove all duplicate rows in the student DataFrame.
# 
# 3. Use the `str.replace` function to remove the "th" from the grade levels in the grade column.
# 
# 4. Check data types using the `dtypes` property.
# 
# 5. Remove the "th" suffix from every value in the grade column using `str` and `replace`.
# 
# 6. Change the grade colum to the `int` type and verify column types.
# 
# 7. Use the head (and/or the tail) function to preview the DataFrame.

# In[21]:


# Check for null values
student_df.isnull().sum()


# In[27]:


# Drop rows with null values and verify removal
student_df = student_df.dropna()

student_df.isnull().sum()


# In[28]:


# Check for duplicated rows
student_df.duplicated().sum()


# In[31]:


# Drop duplicated rows and verify removal
student_df = student_df.drop_duplicates()

student_df.duplicated().sum()


# In[32]:


# Check data types
student_df.dtypes


# In[33]:


# Examine the grade column to understand why it is not an int

student_df.loc[:, "grade"]


# In[34]:


# Remove the non-numeric characters and verify the contents of the column

student_df.loc[:, "grade"] = student_df.loc[:, "grade"].str.replace("th", "")

student_df.loc[:, "grade"]


# In[36]:


# Change the grade column to the int type and verify column types

student_df.loc[:, "grade"] = student_df.loc[:, "grade"].astype("int64")

student_df.dtypes


# ## Deliverable 3: Summarize the Data
# 
# Describe the data using summary statistics on the data as a whole and on individual columns.
# 
# 1. Generate the summary statistics for each DataFrame by using the `describe` function.
# 
# 2. Display the mean math score using the `mean` function. 
# 
# 2. Store the minimum reading score as `min_reading_score`.

# In[37]:


# Display summary statistics for the DataFrame
student_df.describe()


# In[38]:


# Display the mean math score using the mean function
student_df["math_score"].mean()


# In[51]:


# Store the minimum reading score as min_reading_score
min_reading_score = student_df["reading_score"].min()

min_reading_score


# ## Deliverable 4: Drill Down into the Data
# 
# Drill down to specific rows, columns, and subsets of the data.
# 
# To drill down into the data, complete the following steps:
# 
# 1. Use `loc` to display the grade column.
# 
# 2. Use `iloc` to display the first 3 rows and columns 3, 4, and 5.
# 
# 3. Show the rows for grade nine using `loc`.
# 
# 4. Store the row with the minimum overall reading score as `min_reading_row` using `loc` and the `min_reading_score` found in Deliverable 3.
# 
# 5. Find the reading scores for the school and grade from the output of step three using `loc` with multiple conditional statements.
# 
# 6. Using conditional statements and `loc` or `iloc`, find the mean reading score for all students in grades 11 and 12 combined.

# In[40]:


# Use loc to display the grade column

student_df.loc[:, "grade"]


# In[43]:


# Use `iloc` to display the first 3 rows and columns 3, 4, and 5.

student_df.iloc[0:3, [3, 4, 5]]


# In[47]:


# Select the rows for grade nine and display their summary statistics using `loc` and `describe`.

student_df.loc[student_df["grade"] == 9].describe()


# In[54]:


# Store the row with the minimum overall reading score as `min_reading_row`
# using `loc` and the `min_reading_score` found in Deliverable 3.

min_reading_row = student_df.loc[student_df["reading_score"] == min_reading_score]
min_reading_row


# In[132]:


# Use loc with conditionals to select all reading scores from 10th graders at Dixon High School.
# , ["school_name", "reading_score"]

dixon_tenth = student_df.loc[(student_df["grade"] == 10) & (student_df["school_name"] == "Dixon High School")]

dixon_tenth.iloc[:, [2, 3]]


# In[131]:


# Find the mean reading score for all students in grades 11 and 12 combined.

student_df.loc[(student_df["grade"]) > 10, ["reading_score"]].mean()


# ## Deliverable 5: Make Comparisons Between District and Charter Schools
# 
# Compare district vs charter schools for budget, size, and scores.
# 
# Make comparisons within your data by completing the following steps:
# 
# 1. Using the `groupby` and `mean` functions, look at the average reading and math scores per school type.
# 
# 1. Using the `groupby` and `count` functions, find the total number of students at each school.
# 
# 2. Using the `groupby` and `mean` functions, find the average budget per grade for each school type.

# In[138]:


# Use groupby and mean to find the average reading and math scores for each school type.

school_groups = student_df.groupby("school_type").mean()

school_groups.loc[:, ["reading_score", "math_score"]]


# In[161]:


# Use the `groupby`, `count`, and `sort_values` functions to find the
# total number of students at each school and sort from most students to least students.

number_of_students = student_df.groupby("school_name").count()

number_of_students.loc[:, ["student_id"]].sort_values("student_id", ascending = False)


# In[164]:


school_type_grades = student_df.groupby(["school_type", "grade"]).mean()

school_type_grades.loc[:, ["math_score"]]


# # Deliverable 6: Summarize Your Findings
# ### Findings

# Using our analysis, we were able to group dig deeper into our dataset and find out more information about these students than we would've with surface level analysis. Using loc and iloc we could single out certain students or variables to see how they differed across the whole dataset. For example, being able to group up the different types of schools and analyze their scores can give us some insight into how students are faring depending on where they go.
# 
# We can use this code and modified versions of it to see which individual schools are perhaps not performing up to standard and see which grades are suffering the most. In the real world this would be important if we were looking to catch problems before they persisted.

# In[ ]:




