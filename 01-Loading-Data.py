import pandas as pd  # Importing the pandas library

# Reading a CSV file into a DataFrame
data_csv = pd.read_csv("percent_bachelors_degrees_women_usa.csv")

# Printing the entire DataFrame
print(data_csv)

# Reading a text file into a DataFrame with specific separator (comma)
data_txt = pd.read_csv("studentgrades.txt", header=0, sep=',')
# Printing the content of the text file DataFrame
print(data_txt)

# Displaying the first row of the data
print(data_csv.head(1))

# Displaying the last row of the data
print(data_csv.tail(1))

# Displaying general information about the DataFrame (column names, non-null counts, etc.)
print(data_csv.info())

# Accessing the 11th row (index 10) of the DataFrame using iloc
print(data_csv.iloc[10])

# Creating a DataFrame with custom values and row labels (index)
data = pd.DataFrame({
    'A1': [1, 2, 3],
    'A2': [4, 5, 6],
    'A3': [7, 8, 9]
}, index=['X', 'Y', 'Z'])

# Printing the DataFrame
print(data)

# Accessing the row with index 'X'
print(data.loc["X"])

# Accessing all rows, but only the 'A2' column
print(data.loc[:, 'A2'])

# Accessing rows 'Y' and 'Z', and columns 'A1' and 'A2'
print(data.loc[['Y', 'Z'], ['A1', 'A2']])

# Creating another DataFrame with Name, Age, Salary, and Department
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
})

# Printing the DataFrame
print(data)

# Sorting the data based on the 'Salary' column in descending order
print(data.sort_values(by='Salary', ascending=False))
