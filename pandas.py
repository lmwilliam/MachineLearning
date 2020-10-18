# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:53:38 2020

@author: WilliamLiang
"""

import pandas as pd

# In[1] Create a DataFrame

Rows = ["Row1","Row2","Row3"]
Columns = ["Column1","Column2"]

# by list - Row-based
dfList = pd.DataFrame([[1,2],[3,4],[5,6]], index=Rows, columns=Columns)
print("Row-based:", dfList, '\n')

# by Dict - Column-based
dfDict = pd.DataFrame({"Column1":[1,3,5],"Column2":[2,4,6]}, index=Rows)
print("Column-based:", dfDict,)

# In[2] Use CSV to create a DataFrame

dfCSV = pd.read_csv("Carsales.csv")
print(dfCSV)

print(dfCSV["Country"].mode())
print(dfCSV["Age"].median())
print(dfCSV["Salary"].mean())

# In[3] Use HTML to create a DataFrame

dfHTML = pd.read_html("http://www.stockq.org/market/asia.php")
# 7 is an index, you can check the variable explorer to 
# find the index that you want to show. Then you can use
# a slice to show the data. In pandas, there's two variables
# you can use - loc or iloc.
# loc is locator, iloc is index locator.
# [2:, :5]2: means retrive data from second rows to end, 
# :5 means retrive data from 0 to fifth columns.
asia_stocks = dfHTML[7].loc[2:, :5]
print(asia_stocks)

# Turn dataframe to numpy
ary = asia_stocks.values
print(ary)
# In[4] Use a condition to select

dfHTML = pd.read_html("http://www.stockq.org/market/asia.php")
stocks_table = dfHTML[7].loc[2:, [0,1,2,4,5]]

condition = stocks_table[2].astype("float64") > 0
print(stocks_table[condition])