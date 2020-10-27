# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 00:47:07 2020

@author: WilliamLiang
"""

import pandas as pd
import pandas_datareader as pddr
import matplotlib.pyplot as plt
import dateutil.parser as psr

# Recognize traditional Chinese
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus']=False

# Read csv file
dfCSV = pd.read_csv("TaiwanStockID.csv")

# Make sure the input is 1 or 2
while(1):
    print("Please input stock name or stock number.")
    num = input("1 for Stock Name; 2 for Stock Number:")
    num = int(num)
    if(num == 1 or num == 2):
        break
    else:
        continue

# Input stock name or stock number
if(num == 1):
    while(1):
        name = input("Please input your stock name:")
        # Make sure stock name is on the list.
        if(dfCSV.loc[dfCSV['StockName'] == name].empty == True):
            print ("The stock name is not found. Please ensure your input!")
        # Turn stock name to stock number
        else:
            condition = dfCSV["StockName"] == name
            name = dfCSV[condition].iloc[0]["StockID"]
            break
        
elif(num == 2):
    while(1):
        name = input("Please input your stock number:")
        # Make sure input is a integer.
        if(name.isdigit()):
            name = int(name)
            # Make sure stock number is on the list.
            if(dfCSV.loc[dfCSV['StockID'] == name].empty == True):
                print ("The stock number is not found. Please ensure your input!")
            else:
                break
        else:
            print("Please input a Number!")

while(1):
    try:
        while(1):
            # Make sure it is a Date value.
            startDate = psr.parse(input("Please enter start date:"))
            if(psr.parser(startDate)):
                break
            else:
                raise ValueError
        while(1):
            # Make sure it is a Date value.
            endDate = psr.parse(input("Please enter end date:"))
            if(psr.parser(endDate)):
                break
            else:
                raise ValueError
        # Make sure startDate > endDate.
        if(startDate > endDate):
            raise ValueError
        else:
            break
    except ValueError:
        print("ValueError! Please ensure your input is correct.")

# Start query
stock = pddr.DataReader(str(name)+'.TW',"yahoo",startDate,endDate)

# Select the list of closing price
closingPrice = stock["Close"]
closingPrice.plot(label="Closing Price")

# Show monthly and quarterly lines
closingPrice.rolling(window=20).mean().plot(label="20MA")
closingPrice.rolling(window=60).mean().plot(label="60MA")

# Show header
plt.title(str(name)+" "+str(startDate.date())+" ~ "+str(endDate.date())+" Closing Price")
plt.legend(loc="best")

plt.show()