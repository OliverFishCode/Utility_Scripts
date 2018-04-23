# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:51:21 2018

@author: olive
"""

import pandas as pd

data = {'0':[1,2,3,4,5],'1':[2,2,3,2,3]}
df1 = pd.DataFrame(data, columns = ['0','1'])
data2 = {'0':[1,0,1,0,1],'1':[1,1,1,1,1]}
df2 = pd.DataFrame(data2, columns = ['0','1'])
df3 = pd.DataFrame()
def catsr(x):
    if x <= 2:
        return "trib"
    if x > 2 and x <= 5:
        return "ohio"
for col in df1.columns:
    df1[col] = df1[col].apply(lambda x: catsr(x))