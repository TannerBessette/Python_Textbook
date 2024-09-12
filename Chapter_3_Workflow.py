# Use Python as a calculator:
print(1 / 200 * 30)
print((59 + 73 + 2) / 3)

# import numpy for additional mathematics
import numpy as np
print(np.sin(np.pi / 2))

# create new objects with =:
x = 3 * 4
print(x)

# make a list:
primes = [1, 2, 3, 5, 7, 11, 13]
print(primes)

# use list comprehension to do basic arithmetic on list:
[element * 3 for element in primes]

[entry*3 for entry in primes]

# define primes
primes = [1, 2, 3, 5, 7, 11, 13]
# multiply primes by 2
[el * 2 for el in primes]

# typing an object or print(object) both do the same thing
primes
print(primes)

# type() to learn what type of object it is
type(primes)

py_variable = 2 ^ 3

# 3.5 Calling Functions
sum(primes)
sum(primes, start=10)
# ***confused on how the result is 52 here?***

# 3.6 Exercises:
#1
my_variable = 10
my_variable
# did not show at first because object_name was not spelled correctly
#2
import pandas as pd
from palmerpenguins import load_penguins
from lets_plot import *

LetsPlot.setup_html()
penguins = load_penguins()

(
    ggplot(
        data=penguins,
        mapping=aes(x="flipper_length_mm", y="body_mass_g", color="species"),
    )
    + geom_smooth(method="lm")
)
# fixed all erros, all syntax/spelling errors