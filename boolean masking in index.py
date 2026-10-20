import numpy as np
arr=np.array([10,20,30,40,50])
#BASED ON CONDITIONS IT WILL ACESS THE ELEMENTS OF ARRAY  CALLED BOOLEAN MASKING

cond=arr>10
print( "1:",cond) #it will print the condition of array
print( "2:",arr[cond]) #it will print the elements of array which is greater than 10  