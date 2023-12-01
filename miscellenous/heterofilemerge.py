import pandas as pd

df1 = pd.read_csv("customers.csv")
df2 = pd.read_csv("orders.csv")

df = pd.merge(df1,df2,how='outer', on=None, validate="many_to_many")
df1 = df.drop_duplicates()

df2= df1.dropna()

print(df2)
