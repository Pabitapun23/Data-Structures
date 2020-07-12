#Implementation of Linear Search by Python

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = ['p', 'y', 't', 'h', 'o', 'n']
x = 't'
print("The element that is at index is: " +str(linearSearch(arr, x)))