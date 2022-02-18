# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:38:12 2022

@author: Lenovo
"""

from statistics import mean
from scipy import stats
Estimates=[100,500,500,800,3623,5435,42,265,53,3,2666,56]
Estimates.sort()
m=stats.trim_mean(Estimates,0.1)
print(m)