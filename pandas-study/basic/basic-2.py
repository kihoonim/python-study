import pandas as pd

titanic = pd.read_csv('data/titanic.csv')
print(titanic)
print(type(titanic))
print(titanic.head(8))
print(titanic.dtypes)