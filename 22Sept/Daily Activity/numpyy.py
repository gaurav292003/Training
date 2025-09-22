import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1)
print(arr2)

marks= np.array([22,55,43,89,90,58,79])

print("Max Marks", marks.max())
print("Min Marks", marks.min())
print("Average Marks", marks.mean())

print("First three element" ,marks[:3])
print("Reverse element" ,marks[::-1])
print("Sum", np.sum(marks))
print("Standard Deviation", np.std(marks))
