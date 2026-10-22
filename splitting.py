import numpy as np
arr=np.full((1,10),12) #fill the array with 12
print(arr)  
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
#spliting the array wit 2 it will print two arrays with 5 elements each
print(np.split(arr1,2))
arr2=np.array([1,2,3,4,56,7,8,9,10])
print(np.hsplit(arr2)) #spliting the array wit 2 it will print two arrays with 5 elements each


