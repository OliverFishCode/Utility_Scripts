import pandas as pd
import numpy as np
data = np.genfromtxt(r'C:\Users\olive\Google Drive\recruitment manuscript\BaCa_boston_class_clip.csv', delimiter=',', dtype='float',skip_header=1)
data = np.delete(data,0,1)
df1 = pd.DataFrame(data)
data2 = np.genfromtxt(r'C:\Users\olive\Google Drive\recruitment manuscript\SrCa_boston_class_clip.csv', delimiter=',', dtype='float',skip_header=1)
data2 = np.delete(data2,0,1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame()
df4 = pd.DataFrame()

#cols = np.transpose(df1)
#cols2 = pd.DataFrame(cols.index)
#col3 = cols2.index.values
#rows = df3.index.values
def catsr(x):
    if x <= 2:
        return "trib"
    if x > 2 and x <= 5:
        return "ohio"

def catba(x):
    if x <= 1 and x > 0:
        return "lusk"
    if x == 0:
        return "notlusk"
    if x > 1:
        return "emb"

#def catall(Srdf,Badf):
#        d1 = Srdf
#        d2 = Badf
#        y = col3 
#        for y in range (len(col3)):
#            if (d1 is "trib" and d2 is "lusk"):
#                yield  "lusk"
#            if (d1 is "trib" and d2 is "not lusk"):
#                yield "trib"
#            if (d1 is "ohio" and d2 is "lusk" or "notlusk"):
#                yield "ohio"
#
#def rep(rows):  
#        for rows in range(len(df3.index.values)):
#            j = list(catall(df3,df4))
#            yield list(j)        

for col in df1.columns:
    df3[col] = df1[col].apply(catsr)

for col in df2.columns:
    df4[col] = df2[col].apply(catba)


#final_category_proper = pd.DataFrame(list(rep(rows)))

df5 = pd.DataFrame(df3 + df4)

#def catdirty(x):
#    if x == ["triblusk"]:
#        return "lusk"
#    if x is 'ohionotlusk' or x is 'ohiolusk':
#        return 'ohio'
#    if x is "tribnotlusk":
#        return "trib"
#final_cat_dirty = np.where(df5=="triblusk","lusk","none")  

df5 = pd.DataFrame(df5)  
conditions = [
    (df5 == 'ohionotlusk'),
    (df5 == 'ohiolusk'),
    (df5 == 'ohioemb'),
    (df5 == 'triblusk'),
    (df5 == 'tribnotlusk'),
    (df5 == 'tribemb')]
choices = ['ohio','ohio','ohio', 'lusk', 'trib','emb']  
cat_final_np = np.select(conditions, choices, default=np.NaN)






