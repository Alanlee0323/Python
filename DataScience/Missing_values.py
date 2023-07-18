import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

result = df.isna().any()

na_cols=df.columns[df.isna().any()].tolist()
print(na_cols)

mv=pd.DataFrame(df[na_cols].isna().sum(), columns=['Number_missing'])
mv['Percentage_missing']=np.round(100*mv['Number_missing']/len(df),2)
print(mv)