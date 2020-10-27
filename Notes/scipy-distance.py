# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 03:16:53 2020

@author: WilliamLiang
"""

import numpy as np
from scipy.spatial.distance import pdist, squareform

# In[1] Calculate distance

x = np.array([[0,1],[1.,0],[2,0]])

x = pdist(x, 'euclidean')

print(squareform(x))
