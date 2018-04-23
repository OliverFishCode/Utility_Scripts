# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:51:21 2018

@author: olive
"""

import pandas as pd
import numpy as np
data = np.array(([1,2,3,4,5,np.NaN,np.NaN],[2,2,3,2,3,np.NaN,np.NaN]))
data = np.transpose(data)
df1 = pd.DataFrame(data, columns = ['0','1'])
data2 = np.array(([1,1,.5,0,0,np.NaN,np.NaN],[1,0,1,0,1,np.NaN,np.NaN]))
data2 = np.transpose(data2)
df2 = pd.DataFrame(data, columns = ['0','1'])
df3 = pd.DataFrame()

def catsr(x):
    if x <= 2:
        return "trib"
    if x > 2 and x <= 5:
        return "ohio"
for col in df1.columns:
    df3[col] = df1[col].apply(lambda x: catsr(x))