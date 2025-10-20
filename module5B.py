import pandas as pd

student_data1 = {
    'StudentID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Grade': ['A', 'B', 'C']
}

student_data2 = {
    'StudentID': [4, 5, 6],
    'Name': ['David', 'Eva', 'Frank'],
    'Grade': ['B', 'A', 'C']
}

df1 = pd.DataFrame(student_data1)
df2 = pd.DataFrame(student_data2)

combined_df = pd.concat([df1, df2], axis=0)
print(combined_df)
