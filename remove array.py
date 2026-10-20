import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr)

arr_after =np.delete(arr,1) #remove 3 from the array
print(arr_after) #data will change and 3 will be removed from the array

arr1=np.array([[1,2,3],[5,6,7]])
print(arr1)
arr1_after=np.delete(arr1,1,axis=0) #remove 2nd row from the array
print(arr1_after) #data will change and 2nd row will be removed from the

arr2=np.array([[1,2,3],[5,6,7]])
arr2_after=np.delete(arr2,1,axis=1) #remove 2nd column from the array

print(arr2_after) #data will change and 2nd column will be removed from the

arr3=np.array([[1,2,3],[5,6,7]])
arr3_after=np.delete(arr3,1,axis=None) #remove 2nd element from the flattened array
print(arr3_after) #data will change and 2nd element will be removed from the flattened array