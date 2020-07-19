import pandas as pd

# dictionary data
dict_data = {'a': 1, 'b': 2, 'c': 3}

# series data
sr = pd.Series(dict_data)

# show result
print(type(sr))
print('\n')
print(sr)