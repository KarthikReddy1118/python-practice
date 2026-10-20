import numpy as np
arr1=np.array([[1,2,3,4,5,6]])
print(arr1)
print(np.append(arr1,[7,8,9])) 
arr1=np.reshape(arr1,(2,3))  #append 7,8,9 to the end of the array along axis 1
print(arr1) 
print(np.append(arr1,[[7,8,9]],axis=0)) #append 7,8,9 to the end of the array along axis 0
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2) 
print(np.append(arr2,[10,11],axis=1)) #append 10,11,12 to the end of the array along axis 1