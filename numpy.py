# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

@author: WilliamLiang

Github: lmwilliam
"""

import numpy as np

# In[1] Build a 1D array

oneD = np.array([1,2,3])
print(oneD)

# In[2] Build a 2D array

twoD = np.array([[1,2,3],[4,5,6]])
print(twoD)

# In[3] If the data type is different, it will be converted to string type.

differentDataTypes = np.array([15, "Apple", True])
print(differentDataTypes.dtype)

# In[4] Zero array, the default is a floating point number.

zeroArray1 = np.zeros((3,))
print(zeroArray1)

zeroArray2 = np.zeros((2,3))
print(zeroArray2)

# In[5] A constant array of all ones, the default is a floating point number.

constantArray1 = np.ones((3, ))
print(constantArray1)

constantArray2 = np.ones((2, 3))
print(constantArray2)

# In[6] A constant array of all specific number, the default is a floating point number.

constantSNArray1 = np.full((3, ), 4)
print(constantSNArray1)

constantSNArray2 = np.full((2, 3), 4)
print(constantSNArray2)

# In[7] Read and write array elements

readArray = np.array(([1,2,3],[4,5,6]))
print(readArray[0,0], readArray[1,2])

writeArray = np.array(([1,2,3],[4,5,6]))
writeArray[0, 0] = 100
writeArray[1, 2] = 500
print(writeArray)

# In[8] Read array imformations

# Query data type
Array = np.array([[1,2,3],[4,5,6]])
print(type(Array))

# Query data dimensions 
print(Array.ndim)

# Query array shape
print(Array.shape)

# Query elements data type
print(Array.dtype)

# In[9] Linear sample point

linearSample = np.arange(0., 5., 0.2)
print(linearSample)

# Random shuffle
np.random.shuffle(linearSample)
print(linearSample)

# Change sample dimension
linearSample = linearSample.reshape(5, 5)
print(linearSample)

# Change sample data type
linearSample = linearSample.astype("unicode")
print(linearSample)

# Generate "linearly equally spaced" sample points
linearSample = np.linspace(0., 5., 5)
print(linearSample)

# Generate "exponential interval" sample points
linearSample = np.logspace(0., 5., 5)
print(linearSample)

# In[10] Generate "random number" sample points

# Generate integer random number
linearSample2 = np.random.randint(1, 7, size=15)
print(linearSample2)

# Generate floating point random number in [0,1)
linearSample3 = np.random.rand(2,3)
print(linearSample3)

# Generate random number "category data" sample points
# weather: the selected category data list
# size: shape
# replace: True-can be selected repeatedly
# p: Probability of each category of data (Omitted = equal probability of each selection)
weather = ["Sunny", "Cloudy", "Raining", "Windy"]
Taipei = np.random.choice(weather, size=(4, 7), replace=True, p=[0.2, 0.5, 0.2, 0.1])
print(Taipei)

# In[11] Generate "normal distribution" sample points

# Generate a "standard normal distribution"
# Mean = 0, Standard Deviation = 1
standardNormal = np.random.randn(3, 5)
print(standardNormal)

# Generate a "general normal distribution"
# Mean = 10, Standard Deviation = 2
generalNormal = np.random.normal(10, 2, size=(3, 5))
print(generalNormal)

# In[12] Take out "not duplicated" sample points

# Through a Dice for 15 times
dice = np.random.randint(1, 7, size=15)
print(dice)

# Get unique elements
unique = np.unique(dice)
print(unique)

# Get unique elements + counts
unique, count = np.unique(dice, return_counts=True)
print(unique, count)
print(dict(zip(unique, count)))

# In[13] Slicing

oneDslice = np.random.randint(20, size = 20)
print(oneDslice)
print(oneDslice[:5])

twoDslice = np.random.randint(20, size = (5, 5))
print(twoDslice)
print(twoDslice[:2, :2])

# In[14] Statistics

statistics = np.arange(1,11)
print(statistics)

print(statistics.min())
print(statistics.max())
print(statistics.sum())
print(statistics.mean())
print(statistics.std())

# In[15] Array operations

# Array "negative number" & "addition and subtraction"
x1 = np.array([1,2,3])
x2 = np.array([20,36,40])

print(np.negative(x1))
print(np.add(x1, x2))
print(np.subtract(x1, x2))

# Product, dot product, inner product, cross product, outer product
print(np.multiply(x1, x2))
print(np.dot(x1, x2))
print(np.inner(x1, x2))
print(np.cross(x1, x2))
print(np.outer(x1, x2))

# Division, remainder
print(np.divide(x1, x2))
print(np.remainder(x1, x2))

# Matrix division (inverse matrix)
x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)

print(np.dot(x,y))

# Transpose
transpose = np.concatenate((x1, x2)).reshape(2,3).T

print(transpose)

# In[16] Common functions

# Decimal rounding function
num1 = np.array([-1.67, -1.01, -0.35, 0.97, 1.63])

print(np.around(num1, decimals=1))
print(np.floor(num1))
print(np.ceil(num1))

# Exponential correlation function
num2 = np.arange(2, 20, 2).reshape(3, 3)
print(num2)

print(np.power(num2, num2))
print(np.exp2(num2))
print(np.exp(num2))
print(np.sqrt(num2))

# Logarithmic correlation function
print(np.log10(num2))
print(np.log2(num2))
print(np.log(num2))

# Trigonometric function
deg = np.array([0, 30, 60, 90])
rad = np.deg2rad(deg)
print(np.rad2deg(rad))

print(np.sin(rad))
print(np.cos(rad))
print(np.tan(rad))