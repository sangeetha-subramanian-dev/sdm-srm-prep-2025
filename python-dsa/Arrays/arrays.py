from array import *
import numpy as np

arr1 = array('i', [1,2,3,4,5,6]) #S=O(n)
arr2 = array('d', [1.2,1.4,1.6,7.2])
## Traversal in an array
def traverseArray(array): 
    for i in array: # T=O(n)
        print(i)

traverseArray(arr1)


def accessElement(array,index):
    if index > len(array):
        print('There is not any elemetn in the index')
    for i in range(0,len(array)-1): #T=O(n)
        print(array[i])

accessElement(arr1,6)

def linearSearchElement(array,num):
    for i in array: #T=O(n)
        if i==num:
            return i
    return -1
    
print(linearSearchElement(arr1,8))

arr1.remove(1) #T=O(n), S=O(1)
print(arr1)

twoArray = np.array([[1,2],[3,4],[5,6],[7,8]])
print(twoArray)

twoArray=np.insert(twoArray,0,[9,10],axis=0)
print(twoArray)