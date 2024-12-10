import pandas as pd

# Sample DataFrame
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
})

# 1. Mean of numeric columns
print(data['Age'].mean())   # Mean Age
print(data['Salary'].mean())  # Mean Salary

# 2. Median of numeric columns
print(data['Age'].median())  # Median Age
print(data['Salary'].median())  # Median Salary

# 3. Standard deviation of numeric columns
print(data['Salary'].std())  # Standard Deviation of Salary

# 4. Min and Max of numeric columns
print(data['Salary'].min())  # Minimum Salary
print(data['Salary'].max())  # Maximum Salary

# 5. Count of non-null values
print(data['Salary'].count())  # Count of non-null Salary values

# 6. Descriptive statistics for numeric columns
print(data.describe())

# 7. Quantiles (for example, the 25th percentile)
print(data['Salary'].quantile(0.25))

# 8. Skewness (measure of asymmetry)
print(data['Salary'].skew())

# 9. Kurtosis (measure of "tailedness")
print(data['Salary'].kurt())
