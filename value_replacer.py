import pandas as pd
import numpy as np
data = np.array(([1,2,3,4,5,45,np.NaN,np.NaN],[2,2,3,2,np.NaN,np.NaN,np.NaN,np.NaN],[4,4,2,5,1,np.NaN,np.NaN,np.NaN]))
df1 = pd.DataFrame(data, columns = ['0','1','2','3','4','5','6','7'])
nan_count = df1.isnull().sum(axis=1)
df2 = pd.DataFrame()

df2 = df1.where(df1.shift(-2, axis=1).notnull())
