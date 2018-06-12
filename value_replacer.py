import pandas as pd
import numpy as np
data = np.genfromtxt(r'C:\Users\olive\Google Drive\recruitment manuscript\SrCa_new_class.csv', delimiter=',', dtype='float',skip_header=1)
data = np.delete(data,0,1)
df1 = pd.DataFrame(data)
df1 = df1.replace(-1, np.nan)
nan_count = df1.isnull().sum(axis=1)
df2 = pd.DataFrame()
df2 = df1.where(df1.shift(-4, axis=1).notnull())
