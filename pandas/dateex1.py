import pandas as pd

# Creating a DataFrame with datetime index
date_rng = pd.date_range(start='2022-01-01', end='2022-01-05', freq='D')
data = {'values': [10, 15, 20, 25, 30]}
df = pd.DataFrame(data, index=date_rng)

print("DataFrame with DateTimeIndex:")
print(df)
