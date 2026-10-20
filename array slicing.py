import numpy as np
arr=np.array([100,200,300,400,500])
''' it work with m ain three conditions
1. start:stop:step
2. start:stop wont print stop-1 alone print
3.step if wont give step it will take default element as 1'''
print(arr[0:3])

print(arr[0:]) #print all elements from 0 to end
print(arr[ :4]) #print all elements from 0 to 4
print(arr[0:5:2]) #print elements from 0 to 5 with a step of 2

print(arr[::2]) #print all elements with a step of 2    
print(arr[-1:-3])
print(arr[-1:-4:-2]) #print elements from -1 to -4 with a step of -2])
