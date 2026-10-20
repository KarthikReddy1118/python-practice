import numpy as np  
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flatted_array = array.flatten()
print( "Flattened array:", flatted_array)
latted_array2 = array.ravel()
print( "Raveled array:", latted_array2) 
# difference between flatten and ravel is that flatten returns a copy of the original array, while ravel returns a flattened view of the original array whenever possible.  