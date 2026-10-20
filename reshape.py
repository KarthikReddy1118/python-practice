import numpy as np
arr=np.array([1,2,3,4,5,6])

#reshape means we change the shape of the array without changing its data. The total number of elements must remain the same.
print(arr.reshape(2,3)) #reshape to 2 rows and 3 columns
arr2=np.full((1,6),7)
print(arr2.reshape(3,2)) #create a 1x6 array filled with 7s
