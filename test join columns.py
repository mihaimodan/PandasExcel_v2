import pandas as pd
srs_a = pd.Series([1,3,6,8,9])
srs_b = pd.Series(['red', 'green', 'blue', 'white', 'black'])
df = pd.DataFrame({'a': srs_a, 'b': srs_b})
print(df)