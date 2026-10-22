import numpy as np
arr=np.array([1,2,3])
arr2=np.array([5,6])
print(np.concatenate((arr,arr2))) #concatenate arr and arr2
print(np.concatenate((arr,arr2),axis=0)) #concatenate arr and arr2 along axis 0
print(np.concatenate((arr,arr2),axis=1)) #concatenate arr and arr2 along axis 1`