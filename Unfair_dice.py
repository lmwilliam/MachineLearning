# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 02:30:32 2020

@author: WilliamLiang
"""

"""
Homework1: Simulate sample points of "unfair dice"
Assuming there is an "unfair dice", the probability of each side being rolled is as follows:
• 1: 0.1, 2: 0.1, 3: 0.2, 4: 0.1, 5: 0.2, 6: 0.3
Please simulate this dice roll 100 times, and print the simulation result. As follows:
• [5 6 3 2 3 6 6 6 6 3 5 …… 6 5 3 4 3 4]
Please calculate the probability of each point based on the simulation result and compare it with the original theoretical probability. As follows:
• Theoretical probability: {1: 0.1, 2: 0.1, 3: 0.2, 4: 0.1, 5: 0.2, 6: 0.3}
• Actual probability: {1: 0.16, 2: 0.09, 3: 0.26, 4: 0.05, 5: 0.22, 6: 0.22}
"""

import numpy as np

unfairDice = np.arange(1,7)
theoreticalDice = np.random.choice(unfairDice, size = (1,100),replace = True, p = [0.1, 0.1, 0.2, 0.1, 0.2, 0.3])
print("Roll 100 unfair dice simulation results:",'\n',theoreticalDice,'\n')
uniqueDice = np.unique(theoreticalDice)
uniqueDice, countDice = np.unique(theoreticalDice, return_counts = True)
print("Theoretical probability: {1: 0.1, 2: 0.1, 3: 0.2, 4: 0.1, 5: 0.2, 6: 0.3}", '\n')
print("Actual probability:",dict(zip(uniqueDice, countDice / 100)))