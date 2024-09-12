# Import necessary packages
import pandas as pd
from lets_plot import *
from palmerpenguins import load_penguins

# Set up LetsPlot to work in HTML
LetsPlot.setup_html()

# Load the penguins dataset
penguins = load_penguins()
penguins.head()

#2.2.3 Creating a Plot
gg = (
    ggplot(data=penguins, mapping=aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point(aes(color="species", shape="species"))
    + geom_smooth(method="lm")
    + labs(
        title="Body mass and flipper length",
        subtitle="Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
        x="Flipper length (mm)",
        y="Body mass (g)",
        color="Species",
        shape="Species",
    )
)

gg_1.show()

#2.2.5 Exercises
#1. 344 rows, 8 columns
#2. (penguins data does not have a help option) 
#3. In general, longer bill length, lower the bill depth. Not a strong correlation.
gg_1 = (
    ggplot(data=penguins, mapping=aes(x="bill_length_mm", y="bill_depth_mm"))
    + geom_point(aes())
    + geom_smooth(method="lm")
    + labs(
        title="Bill depth vs. bill length",
        subtitle="Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
        x="Bill length (mm)",
        y="Bill depth (mm)",
        color="Species",
        shape="Species",
    )
)
#4. a bar plot would be a better option
(
    ggplot(data=penguins, mapping=aes(x="species", y="bill_depth_mm"))
    + geom_point(aes())
    + geom_smooth(method="lm")
    + labs(
        title="Bill depth vs. species",
        subtitle="Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
        x="Bill length (mm)",
        y="Bill depth (mm)",
        color="Species",
        shape="Species",
    )
)
#5. there are no x or y aesthetics, need to specify what to put points for
(
    ggplot(data = penguins, mapping = aes(x = "bill_length_mm", y = "species")) + 
        geom_point() +
        labs(caption = 'Data come from the palmerpenguins package.' )
)
#6. (added to the plot above with the caption labs option)
#7. cannot see the visualization we are supposed to replicate
#8. 
(ggplot(
  data = penguins,
  mapping = aes(x = "flipper_length_mm", y = "body_mass_g", color = "island")
) +
  geom_point() +
  geom_smooth(se = False)
)
#9. no, they will look the same because despite the smoothing specifications,
 # there will only be one smoothing line

#2.3: (do not need to specify data or mapping, since those are default first 2)
(
    ggplot(penguins, aes(x = "flipper_length_mm", y = "body_mass_g")) + 
  geom_point()
)

#2.4.1
(ggplot(penguins, aes(x="species")) + geom_bar())

# transform a variable to categorical like using pandas:
penguins["species"] = penguins["species"].astype("category")
penguins.head()

# historgram plot:
(ggplot(penguins, aes(x="body_mass_g")) + 
    geom_histogram(binwidth=200))

# density plot:
(ggplot(penguins, aes(x="body_mass_g")) + geom_density())

# 2.4.3 Exercises
# quotes for variable, single quote for string in python
#1
(ggplot(penguins) + 
    geom_bar(aes(y = "species")))
# it makes the bars go from the side instead of the bottom

#2 (another error in textbook, no quotes around species)
(ggplot(penguins, aes(x = "species")) +
  geom_bar(color = "red"))
# color does the outside, fill fills the insides of the bars
(ggplot(penguins, aes(x="body_mass_g")) + 
    geom_histogram(bins = 5))
#3
# bins makes 5 equal width bins

# 2.5.1
# to visualize numerical and categorical variable relationship 
# we can use side by side boxplots
# IQR is from 25th to 75th percentile
# any points over 1.5 times the IQR appear as points above boxplot
# line from boxplots goes out to farthest non-outlier
(ggplot(penguins, aes(x="species", y="body_mass_g")) + 
    geom_boxplot())

# probability density plot instead of boxplot:
(ggplot(penguins, aes(x="body_mass_g", color="species")) + 
    geom_density(size=2))

# alpha adds transparency, can fill and color with same value:
(ggplot(penguins, aes(x="body_mass_g", color="species", fill="species")) +
    geom_density(alpha=0.5))

#2.5.2
# stacked bar plots visualize relationship between two categorical vars.
(ggplot(penguins, aes(x="island", fill="species")) + 
    geom_bar())

# relative frequency plot instead of total count:
(ggplot(penguins, aes(x="island", fill="species")) + 
    geom_bar(position="fill") + labs(y = 'Penguin Frequency'))

#2.5.3
# scatterplot for two numerical variables:
(ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g")) + 
    geom_point())

# three or more variables:
(ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point(aes(color="species", shape="island"))
)

# facet_wrap to facet by a single variable if too many vars. 
# gets messy-looking:
(ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point(aes(color="species", shape="species"))
    + facet_wrap(facets="island")
)

# 2.5.5 Exercises:
# 1
(ggplot(penguins, aes(x="bill_length_mm", y="bill_depth_mm")) + 
    geom_point() +
    facet_wrap(facets = "species"))
# adele tend to have shorter bill lengths, gentoo shorter bill depths

# 2.
(
    ggplot(
      data = penguins,
      mapping = aes(
        x = "bill_length_mm", y = "bill_depth_mm", 
        color = "species", shape = "species"
      )
    ) +
      geom_point() +
      labs()
)
# remove the color argument from labs()

#3. # another textbook error, no parentheses around outside of ggplot
(ggplot(penguins, aes(x = "island", fill = "species")) +
  geom_bar(position = "fill"))
# proportion of island penguins that are each species
(ggplot(penguins, aes(x = "species", fill = "island")) +
  geom_bar(position = "fill"))
# proportion of each species of penguin that live on each island

# ggsave to save plots as images using format svg:
# can update image size with scale argument if using raster format
plotted_data = (ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g")) +
    geom_point()
)
ggsave(plotted_data, scale = 3.0, filename="penguin-plot.svg")
# having trouble with adjusting saved image size
