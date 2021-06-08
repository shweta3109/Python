import pandas as pd
df = pd.read_csv("C:/Users/Shweta/Downloads/data.csv")
x = df["Pulse"].mode()[0]
df["Pulse"].fillna(x, inplace = True)