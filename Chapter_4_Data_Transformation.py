# data transformation using pandas package
# goal of chapter is overview of tools to transform dataframe
import pandas as pd

# figured out other way to import the data
url = '/Users/tannerbessette/Desktop/flights.csv'
flights = pd.read_csv(url)
flights.head
flights.info

#DATA TYPES IN PYTHON
# float64 --> real numbers
# category --> categories
# datetime64 --> date times
# int64 --> integers
# bool --> True or False
# string --> text

flights["time_hour"] = pd.to_datetime(flights["time_hour"], format="%Y-%m-%dT%H:%M:%SZ")


# 4.2
# Example dataframe:
df = pd.DataFrame(
    data={
        "col0": [0, 0, 0, 0],
        "col1": [0, 0, 0, 0],
        "col2": [0, 0, 0, 0],
        "col3": ["a", "b", "b", "a"],
        "col4": ["alpha", "gamma", "gamma", "gamma"],
    },
    index=["row" + str(i) for i in range(4)],
)
df.head()

# use pandas to do multiple assignments in a single command
# FOR ME:
# query() is like filter in R
# groupby() is like group_by() in R

# last part of this line of code is to specify the groupby() operation .mean()
(flights.query("dest == 'IAH'").groupby(["year", "month", "day"])[["arr_delay"]].mean())

#4.3 Manipulating Rows in Data Frames
import numpy as np

df = pd.DataFrame(
    data=np.reshape(range(36), (6, 6)),
    index=["a", "b", "c", "d", "e", "f"],
    columns=["col" + str(i) for i in range(6)],
    dtype=float,
)
df["col6"] = ["apple", "orange", "pineapple", "mango", "kiwi", "lemon"]
df

# To access a particular row directly, you can use df.loc['rowname'] or 
# df.loc[['rowname1', 'rowname2']] for multiple rows

# can also access rows by: (**PYTHON STARTS AT ZERO NOT 1**)
df.iloc[0]

#4.3.2 filter rows with query:
df.query("col6 == 'kiwi' or col6 == 'pineapple'")
# FOR ME: or instead of | in R, quotes around whole query line of code
# and instead of & in R

# even with math, quotes around everything in the parentheses
df.query("col0 > 6")

# Flights that departed on January 1
# = and == same as R
flights.query("month == 1 and day == 1")

# 4.3.3 re-arranging rows
# .sort_values() in pandas is similar to arrange() in R
flights.sort_values(["year", "month", "day", "dep_time"])

# can add ascending = FALSE similar to order in descending order:
flights.sort_values("dep_delay", ascending=False)

# top three destinations of the flights that were most delayed on arrival 
# that left on roughly on time
(
    flights.query("dep_delay <= 10 and dep_delay >= -10")
    .sort_values("arr_delay", ascending=False)
    .iloc[[0, 1, 2]]
)

# 4.3.4 Exercises
# 1a.
flights.query("arr_delay >= 120")
# 1b.
flights.query("dest == 'IAH' or dest == 'HOU'")
# 1c.
flights.query("carrier == 'UA' or carrier == 'DL'")
# 1d.
flights.query("month == 7 or month == 8 or month == 8")
# 1e.
flights.query("dep_delay <= 0 and arr_delay >= 120")
# 1f.
flights.query("dep_delay >= 60 and arr_delay <= 30")

# 2. 
flights.sort_values("dep_delay", ascending=False)
# flight 7072 and flight 235778

# 3.
flights.sort_values("air_time", ascending=True)
# 20 minutes is the fastest flight

# 4.
flights.sort_values("distance", ascending=False)
# 4983 miles are the furthest flights

# FOR ME:
# remember, False and True instead of FALSE and TRUE in R

#5
# It makes more sense to use query first, since it will filter to
# only include the rows you want, and then sort from those rows after
# with .sort_values()


#4.4.1 creating new columns:
df["new_column0"] = 5
df

df["new_column0"] = [0, 1, 2, 3, 4, 5]
df

# Exercise: ValueError if too many or too few

# create more than one column:
df[["new_column1", "new_column2"]] = [5, 6]
df

# Create column that is a result of operation of existing columns
df["new_column3"] = df["col0"] - df["new_column0"]
df

# can also do this with assign()
# lambda argument means you want to do the operation with all rows
(
    flights.assign(
        gain=lambda row: row["dep_delay"] - row["arr_delay"],
        speed=lambda row: row["distance"] / row["air_time"] * 60,
    )
)

# 4.4.2 Accessing Columns
# select multiple columns to access using a list:
df[["col0", "new_column0", "col2"]]

# use .loc to access particular rows at the same time:
df.loc[["a", "b"], ["col0", "new_column0", "col2"]]

# can access columns similarly by using iloc
df.iloc[:, [0, 1]]

# (this chapter skips over slicing, but that is another option)

# select column based on data type:
flights.select_dtypes("int")

# non-pandas way to select columns based on criteria such as names
print("The list of columns:")
print(df.columns)
print("\n")

print("The list of true and false values:")
print(df.columns.str.startswith("new"))
print("\n")

print("The selection from the data frame:")
df.loc[:, df.columns.str.startswith("new")]


# 4.4.3 Renaming Columns
# view rename
df.rename(columns={"col3": "letters", "col4": "names", "col6": "fruit"})
# (just showing, not saving, would need to add df = on left)

# rename all columns:
df.columns = df.columns.str.capitalize()

# replacing specific parts of column names:
df.columns.str.replace("Col", "Original_column")


# 4.4.4 Re-ordering columns
# fresh data from before:
df = pd.DataFrame(
    data=np.reshape(range(36), (6, 6)),
    index=["a", "b", "c", "d", "e", "f"],
    columns=["col" + str(i) for i in range(6)],
    dtype=float,
)
df

# re-order by using a list:
df = df[["col5", "col3", "col1", "col4", "col2", "col0"]]
df


# 4.5.1 Column and Row Exercises:
# 1.
flight_time = flights["arr_time"] - flights["dep_time"]
flight_time
flights["air_time"]
# it looks like it is treating 10:04 as 1004, which is going to mean
# every 60 mins is being treated as 100 in the air_time var. in flights dataset
# 2.
flights[["dep_time", "sched_dep_time", "dep_delay"]]
# I would expect dep_time - sched_dep_time = dep_delay which is true
# 3.
# you could use .isin(), str.contains(), or just use a basic list df[[]]
# 4.
flights[["air_time", "air_time"]]
# it just duplicates the row however many times you include it when
# trying to select
# 5.
flights.columns.isin(["year", "month", "day", "dep_delay", "arr_delay"])
# it appears to be checking the list of columns to see if each entry 
# matches the entry from the .isin() call, and outputting a true 
# or false based on whether they match
# 6:
flights.loc[:, flights.columns.str.contains("time")]
# yes the result surprised me at first, it is because Python is case sensitive
# so fixing that issue resolves the error 


# MAYBE POTENTIAL DATASETS?:
# 1. Top Universities Ranking 2024 - Kaggle dataset
# 2. Olympic Summer Games - Paris 2024 - Kaggle dataset
#         - has lots of other .csv in it including medals, results, etc.

# 4.6 Grouping, Changing Index, and Applying 
(flights.groupby("month")[["dep_delay"]].mean())

# multiple summary operations in one go: (using agg)
(flights.groupby("month")[["dep_delay"]].agg("mean"))

# For doing multiple aggregations on multiple columns with new names for the 
# output variables, the syntax becomes:
(
    flights.groupby(["month"]).agg(
        mean_delay=("dep_delay", "mean"),
        count_flights=("dep_delay", "count"),
    )
)

# group by multiple vars.:
month_year_delay = flights.groupby(["month", "year"]).agg(
    mean_delay=("dep_delay", "mean"),
    count_flights=("dep_delay", "count"),
)
month_year_delay

# reset index to set the index to the normal 0,1,2,3...
month_year_delay.reset_index()

# remove one layer of index
month_year_delay.reset_index(1)

# 4.6.3: Grouping and transforming:
# use .transform with .groupby to perform computations on groups
# but you want to go back to the original index
flights["max_delay_month"] = flights.groupby("month")["arr_delay"].transform("max")
flights["delay_frac_of_max"] = flights["arr_delay"] / flights["max_delay_month"]
flights[
    ["year", "month", "day", "arr_delay", "max_delay_month", "delay_frac_of_max"]
].head()

# 4.6.4 Exercises
# 1:
average_delays = flights.groupby("carrier")["arr_delay"].mean()
print(average_delays)
# F9 appears to have the worst delays
# it would be hard to disentangle the effects of bad airports vs. bad
# carriers, especially because maybe bad carriers tend to more likely
# be at bad airports or vice versa

# 2:
max_delays = flights.groupby("dest")["arr_delay"].max()
print(max_delays)

max_delays.sort_values()
# HNL is the most delayed flight with 1272 mins

# 3:
flights['dep_hour'] = flights['dep_time'] // 100
average_delay_by_hour = flights.groupby('dep_hour')['arr_delay'].mean()
print(average_delay_by_hour)
# delays appear to be much higher in the early morning hours 
# (some almost 3 hours average!)