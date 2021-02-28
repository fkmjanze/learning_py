import numpy as np
import pandas as pd

list_a = (1, 1, 1, 2, 2, 2, 100, 100, 100, 100)
list_b = (0, 0, 1, 1, 1, 2, 2, 2, 2, 100)

df = pd.DataFrame(list_b)

print(df.median())
print(df.mode())
print(df.mean())

#description = (pd.df_a.median(), pd.df_a.mean(), pd.df_a.mode())
# print(description)
