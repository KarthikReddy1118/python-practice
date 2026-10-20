import numpy as np
arr=np.array([10,20,30,40,50])
print(arr) 
arr_after_insertion= np.insert(arr,2,50) #insert 50 at index 2
print(arr_after_insertion) #heare data wont change it just makes a new array with the inserted value

arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
arr1_after_insertion= np.insert(arr1,1,[99,98,100],axis=0) 
print(arr1_after_insertion) 
arr2=np.array([[1,2,3],[4,5,6]])
arr2_after_insertion= np.insert(arr2,1,[99,98],axis=1)
print(arr2_after_insertion)