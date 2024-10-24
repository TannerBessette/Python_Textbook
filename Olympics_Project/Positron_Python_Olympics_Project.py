import pandas as pd
from palmerpenguins import load_penguins
from lets_plot import *
LetsPlot.setup_html()

# Read in data:
Athletes_df = pd.read_csv("/Users/tannerbessette/Desktop/SYE/athletes.csv")
Medals_df = pd.read_csv("/Users/tannerbessette/Desktop/SYE/medals.csv")


# Create Male and Female Datasets:
Male_Athletes_df = Athletes_df.query("gender == 'Male'")
Female_Athletes_df = Athletes_df.query("gender == 'Female'")


# Total Male and Female Medals for each sport:
# (learned reset_index from ChatGPT - helps to mimick summarise in R)
Male_Total_Medal_Counts = Medals_df.query("gender == 'M'").groupby("country_code").size().reset_index(name = "medal_totals")
Female_Total_Medal_Counts = Medals_df.query("gender == 'W'").groupby("country_code").size().reset_index(name = "medal_totals")


# MALE BAR PLOT:
# data manipulation (group_by, summarise):
Male_Athletes_Count = Male_Athletes_df.groupby("country_code").size().reset_index(name = "athlete_count")
# join data (looked ahead in textbook to ch. 22):
# (pd.merge is the join function, on is like by, how = join method(L/R))
Male_Athletes_Count_joined = pd.merge(Male_Athletes_Count, Male_Total_Medal_Counts, on="country_code", how="left")
# Only keep top 10 countries with most athletes:
Male_Athletes_Count_joined = Male_Athletes_Count_joined.query("athlete_count > 128")
# Create the Male bar plot with country's athletes and medals:
#Male_Athletes_Count.sort_values (essentially arrange -> do instead of reorder)
Male_Athletes_Count_joined = Male_Athletes_Count_joined.sort_values("athlete_count", ascending=False)
(
    ggplot() +
          geom_bar(aes(x = 'country_code', y = 'athlete_count'), fill = "lightblue", stat = "identity", data = Male_Athletes_Count_joined) +
          geom_bar(aes(x = 'country_code', y = 'medal_totals'), fill = "darkblue", stat = "identity", data = Male_Athletes_Count_joined) +
          labs(title = "Male Athletes and Medals by Country",
               x = "Country",
               y = "Male Athletes and Medal Counts") +
          theme_minimal()
)


# FEMALE BAR PLOT:
# data manipulation (group_by, summarise):
Female_Athletes_Count = Female_Athletes_df.groupby("country_code").size().reset_index(name = "athlete_count")
# join data (looked ahead in textbook to ch. 22):
# (pd.merge is the join function, on is like by, how = join method(L/R))
Female_Athletes_Count_joined = pd.merge(Female_Athletes_Count, Female_Total_Medal_Counts, on="country_code", how="left")
# Only keep top 10 countries with most athletes:
Female_Athletes_Count_joined = Female_Athletes_Count_joined.query("athlete_count > 177")
# Create the Male bar plot with country's athletes and medals:
# (arrange first):
Female_Athletes_Count_joined = Female_Athletes_Count_joined.sort_values("athlete_count", ascending=False)
(
    ggplot() +
          geom_bar(aes(x = 'country_code', y = 'athlete_count'), fill = "lightblue", stat = "identity", data = Female_Athletes_Count_joined) +
          geom_bar(aes(x = 'country_code', y = 'medal_totals'), fill = "darkblue", stat = "identity", data = Female_Athletes_Count_joined) +
          labs(title = "Female Athletes and Medals by Country",
               x = "Country",
               y = "Female Athletes and Medal Counts") +
          theme_minimal()
)
