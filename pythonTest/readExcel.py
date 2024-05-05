# pip install openpyxl
# pip install xlrd

import pandas as pd

print(pd.__version__)
# 1.2.2

df = pd.read_excel('./data/Book1.xlsx', index_col=0)
print(df)
#         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33

print(type(df))
# <class 'pandas.core.frame.DataFrame'>
