# avoid unclear abbreviations when naming variables

# for boolean, good to use "is_married" (for ex)

# use descriptive variable names that reveal your intention, 
# eg days_since_treatment

# keep vocab consistent among diff vars.

# avoid noise comments that are obvious from looking at code

# functions come with their own special comments called doc string
def round_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Rounds numeric columns in dataframe to 2 s.f.
    Args:
        df (pd.DataFrame): Input dataframe
    Returns:
        pd.DataFrame: Dataframe with numbers rounded to 2 s.f.
    """
    for col in df.select_dtypes("number"):
        df[col] = df[col].apply(lambda x: float(f'{float(f"{x:.2g}"):g}'))
    return df


# method chaining
import pandas as pd

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


# Chaining inside parentheses works
results = df.groupby(["col3", "col4"]).agg({"col1": "count", "col2": "mean"})
results

# don't repeat yourself by assigning same variable name twice

# don't try to have a single function do everything
# don't use flags/booleans in functions?
