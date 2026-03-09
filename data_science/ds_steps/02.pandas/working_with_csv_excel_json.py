import pandas as pd 
df=pd.read_csv("files/data.csv")
df=df[df['Age']>21]
df.to_csv("files/output.csv", index=False)