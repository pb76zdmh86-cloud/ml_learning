import pandas as pd

df = pd.read_csv('apartments.csv')
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
areas = df['area']
price_areas = df[["area", "price"]]
print(price_areas)
print(areas)
print(df.head(3))
print(areas.shape)
print(price_areas.shape)