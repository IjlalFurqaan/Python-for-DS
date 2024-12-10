import pandas as pd

data_csv=pd.read_csv("percent_bachelors_degrees_women_usa.csv")

print(data_csv)



data_txt = pd.read_csv("studentgrades.txt", header=0, sep=',')
print(data_txt)

print(data_csv.head(1))
print(data_csv.tail(1))
print(data_csv.info())

print(data_csv.iloc[10])

data = pd.DataFrame({
    'A1': [1, 2, 3],
    'A2': [4, 5, 6],
    'A3': [7, 8, 9]
}, index=['X', 'Y', 'Z'])


print(data)
print(data.loc["X"])
print(data.loc[:, 'A2'])
print(data.loc[['Y', 'Z'], ['A1', 'A2']])
