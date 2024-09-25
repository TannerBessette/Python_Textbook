# melting allows you to change the form of your data
# without changing any of the values
# row <-> observation, variable <->column, value <-> cell

# example of melt in action:
import pandas as pd

df = pd.DataFrame(
    {
        "first": ["John", "Mary"],
        "last": ["Doe", "Bo"],
        "job": ["Nurse", "Economist"],
        "height": [5.5, 6.0],
        "weight": [130, 150],
    }
)
print("\n Unmelted: ")
print(df)
print("\n Melted: ")
df.melt(id_vars=["first", "last"], var_name="quantity", value_vars=["height", "weight"])

# Exercise:
# Perform a melt() that uses job as the id instead of first and last
df = pd.DataFrame(
    {
        "first": ["John", "Mary"],
        "last": ["Doe", "Bo"],
        "job": ["Nurse", "Economist"],
        "height": [5.5, 6.0],
        "weight": [130, 150],
    }
)
print("\n Unmelted: ")
print(df)
print("\n Melted: ")
df.melt(id_vars=["job"], var_name="quantity", value_vars=["height", "weight"])

# 6.3.2 Wide to Long
# useful for data where there are different vars. and time periods across columns
import numpy as np

df = pd.DataFrame(
    {
        "A1970": {0: "a", 1: "b", 2: "c"},
        "A1980": {0: "d", 1: "e", 2: "f"},
        "B1970": {0: 2.5, 1: 1.2, 2: 0.7},
        "B1980": {0: 3.2, 1: 1.3, 2: 0.1},
        "X": dict(zip(range(3), np.random.randn(3))),
        "id": dict(zip(range(3), range(3))),
    }
)
df

pd.wide_to_long(df, stubnames=["A", "B"], i="id", j="year")

# 6.3.3 Stack and Unstack
# stack and unstack
# stack is a shortcut for taking a single type of wide data variable
# from columns and turning it into a long form dataset but with an extra index
# example dataset
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df

# stack this to create a tidy dataset:
df = df.stack()
df

# unstack example
df.unstack(level=0)

# Exercise: unstack level = 1 appears to be doing the same thing as level = 0
# for this example

# 6.3.4 Pivoting
import numpy as np

data = {
    "value": np.random.randn(20),
    "variable": ["A"] * 10 + ["B"] * 10,
    "category": np.random.choice(["type1", "type2", "type3", "type4"], 20),
    "date": (
        list(pd.date_range("1/1/2000", periods=10, freq="M"))
        + list(pd.date_range("1/1/2000", periods=10, freq="M"))
    ),
}
df = pd.DataFrame(data, columns=["date", "variable", "category", "value"])
df.sample(5)

df.pivot(index="date", columns="variable", values="value").shift(1)

# To go back to the original structure, albeit without the category columns, 
# apply .unstack().reset_index().

# Exercise:
# Perform a pivot() that applies to both the variable and category columns:
df.pivot(index="date", columns=["variable", "category"], values="value")
pivoted_df = df.pivot(index="date", columns=["variable", "category"], values="value")
# not sure what the result was supposed to look like -> this may be right
