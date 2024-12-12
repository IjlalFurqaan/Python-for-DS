import pandas as pd

employees = pd.DataFrame({
    'EmployeeID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'DepartmentID': [1, 2, 3]
})


departments = pd.DataFrame({
    'DepartmentID': [1, 2, 4],
    'DepartmentName': ['HR', 'IT', 'Marketing']
})

result = pd.merge(employees, departments, on='DepartmentID', how='left')
print("Merged DataFrame:\n", result)