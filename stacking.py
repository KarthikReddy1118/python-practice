import numpy as np
arr=np.array([1,2,3])
arr1=np.array([4,5,6])
print(np.stack((arr,arr1))) #stack arr and arr1 
#stacking means joinig the arrays along a new axis

print(np.vstack((arr1,arr))) #stack arr and arr1 vertically

print(np.hstack((arr,arr1))) #stack arr and arr1 horizontally

'''
heare bot vertican amd norizontal stacking is done along the existing axis, whereas stacking is done along a new axis.'''