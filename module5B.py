#EX 1
import numpy as np

arr = np.array([[5, 2, 9],
                [1, 8, 3],
                [4, 7, 6]])

sorted_arr = np.sort(arr, axis=0)

print("Original array:\n", arr)
print("Column-wise sorted array:\n", sorted_arr)

#EX 2
import numpy as np

x = np.array([3, 7, 5, 9, 2])
y = np.array([2, 7, 8, 1, 2])

indices = np.where(x >= y)
print("Indices where x >= y:", indices[0])

#EX 3
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

new_col = np.array([10, 11, 12])

arr = np.delete(arr, 1, axis=1)
arr = np.insert(arr, 1, new_col, axis=1)

print("Updated array:\n", arr)

#EX 4
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, 12, 9, 20, 14.5, 13, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print(df)

#EX 5
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
