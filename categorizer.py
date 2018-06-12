import pandas as pd
import numpy as np
data = np.genfromtxt(r'C:\Users\olive\Google Drive\recruitment manuscript\BaCa_new_class_clip.csv', delimiter=',', dtype='float',skip_header=1)
data = np.delete(data,0,1)
df1 = pd.DataFrame(data)
data2 = np.genfromtxt(r'C:\Users\olive\Google Drive\recruitment manuscript\SrCa_new_class_clip.csv', delimiter=',', dtype='float',skip_header=1)
data2 = np.delete(data2,0,1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame()
df4 = pd.DataFrame()
del (data,data2) 

def catsr(x):
    if x <= 0.3905126:
        return "trib"
    if x > 0.3905127 and x <= 0.5137543:
        return "mmr_trib"
    if x > 0.5137544 and x <= 0.5695187:
        return "unknown"
    if x > 0.5695188 and x <= 0.9315134:
        return "mmr_ohio"
    if x > 0.9315135 and x <= 1.1580521:
        return "union"
    if x > 1.1580522 and x <= 10000:
        return "outside"
    else:
        return "none"
    
def catba(x):
    if x >0.0033974 and  x <= 0.005684436:
        return "_def_trib"
    if x > 0.005684437 and x <= 0.00818352:
        return "_ohio_trib"
    if x > 0.008183521 and x <= 0.012092914:
        return "_mmr_trib"
    else:
        return "_none"


for col in df1.columns:
    df3[col] = df2[col].apply(catsr)

for col in df2.columns:
    df4[col] = df1[col].apply(catba)




df5 = pd.DataFrame(df3 + df4)


df5 = pd.DataFrame(df5)  
conditions = [
    (df5 == 'mmr_ohio_def_trib'),
    (df5 == 'mmr_ohio_none'),
    (df5 == 'mmr_ohio_ohio_trib'),
    (df5 == 'mmr_ohio_mmr_trib'),  
    (df5 == 'union_def_trib'),
    (df5 == 'union_none'),
    (df5 == 'union_ohio_trib'),
    (df5 == 'union_mmr_trib'),   
    (df5 == 'outside_def_trib'),
    (df5 == 'outside_none'),
    (df5 == 'outside_ohio_trib'),
    (df5 == 'outside_mmr_trib'), 
    (df5 == 'none_def_trib'),
    (df5 == 'none_none'),
    (df5 == 'none_ohio_trib'),
    (df5 == 'none_mmr_trib'),
    (df5 == 'unknown_def_trib'),
    (df5 == 'unknown_none'),
    (df5 == 'unknown_ohio_trib'),
    (df5 == 'unknown_mmr_trib'),  
    (df5 == 'trib_def_trib'),
    (df5 == 'trib_none'),
    (df5 == 'trib_ohio_trib'),
    (df5 == 'trib_mmr_trib'),
    (df5 == 'mmr_trib_def_trib'),
    (df5 == 'mmr_trib_none'),
    (df5 == 'mmr_trib_ohio_trib'),
    (df5 == 'mmr_trib_mmr_trib'),
    ]

choices = ['mmr_ohio',
           'mmr_ohio',
           'ohio',
           'mmr',           
           'union',
           'union',
           'union',
           'union',         
           'outside',
           'outside',
           'outside',
           'outside',         
           'trib',
           '0',
           'ohio_trib',
           'mmr_trib',         
           'trib',
           'unknown',
           'ohio_trib',
           'mmr_trib',           
           'trib',
           'trib',
           'trib',
           'trib',           
           'trib',
           'mmr_trib',
           'trib',
           'mmr_trib',
           ]  
cat_final_np = np.select(conditions, choices, default=np.NaN)
cat_final = pd.DataFrame(cat_final_np)





