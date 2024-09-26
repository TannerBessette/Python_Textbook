import pandas as pd
# pd.read_csv() is the same as read_csv() in R

# load a dataset (csv):
# students = pd.read_csv("data/students.csv")

# check which folder you are currently in:
import os
os.getcwd()  # get current working directory (cwd)

# when reading in a csv:
# skiprows = n to skip the first n lines 
# names =     to set names of columns i.e. names = range(5) for 0 to 4

from skimpy import clean_columns

print(os.listdir())
students = pd.read_csv("students_data.csv")
students

# clean_columns converts variable names to snake case
students = clean_columns(students)
students

# cast favorite food variable to be string only
# (fixes the NaN value to a <NA>)
students["favourite_food"] = students["favourite_food"].astype("string")

# change five to 5 with .replace:
students["age"] = students["age"].replace("five", 5)
# view just the age column to observe the correction
students["age"]


# make meal plan a categorical variable (has a known set of poss. values)
students["meal_plan"] = students["meal_plan"].astype("category")
students["meal_plan"]

# ** side note: using [] instead of $ in python to specify a dataset's variable
# that we are changing **

# pass a dictionary to map columns to variable type:
# (assigning the type of each var. as int, string, etc.):
students = students.astype({"student_id": "int", "full_name": "string", "age": "int"})
students.info()


# Exercise:
# 1. you would use the sep argument, in the usual pd.read_csv(), 
#    specifically, you would use 
#    students = pd.read_csv("students.csv", sep = "|")


# STUFF BELOW ARE ALL THINGS I HAVE NOT DONE IN R:
# reading data from multiple files, and stacking them on top of each other
# in a single dataframe using pd.concat():
#list_of_dataframes = [
#    pd.read_csv(x)
#    for x in ["data/01-sales.csv", "data/02-sales.csv", "data/03-sales.csv"]
#]
#sales_files = pd.concat(list_of_dataframes)
#sales_files

# can use glob to find files for you, so you don't have to specify
# the name of many datasets

# write our data as a csv file:
students.to_csv("students-clean.csv")
pd.read_csv("students-clean.csv").info()
# we lost our assignment of variable types
# (I remember this happening in R too)

# need to use a diff data format for it to remember data types
# textbook recommends using the feather format
# writing to a feather file:
students.to_feather("students-clean.feather")
# reopen that feather file and look at info attached:
pd.read_feather("students-clean.feather").info()
# it successfully remembered our variable types

# For non-csv, there are many pandas options for importing, 
# similar to R, such as read_json, read_html, etc.