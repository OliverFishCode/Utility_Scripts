
import pandas as pd
import numpy as np
data = np.array(([1,2,3,4,5,5,np.NaN,np.NaN],[2,2,3,2,np.NaN,np.NaN,np.NaN,np.NaN],[4,4,2,5,1,np.NaN,np.NaN,np.NaN]))
df1 = pd.DataFrame(data, columns = ['0','1','2','3','4','5','6','7'])
data2 = np.array(([1,1,.5,0,0,np.NaN,np.NaN],[1,0,1,0,1,np.NaN,np.NaN]))
df2 = pd.DataFrame(data2, columns = ['0','1','2','3','4','5','6'])
df3 = pd.DataFrame()

def catsr(x):
    if x <= 2:
        return "trib"
    if x > 2 and x <= 5:
        return "ohio"
for col in df1.columns:
    df3[col] = df1[col].apply(lambda x: catsr(x))