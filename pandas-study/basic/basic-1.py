import pandas as pd

df = pd.DataFrame({
    'Name' : ['A', 'B', 'C'],
    'Age' : [22, 35, 58],
    'Sex' : ['male', 'male', 'female']
})

print(df)
print(df['Age'])
ds = df.describe()
print(ds)
print(type(ds))
