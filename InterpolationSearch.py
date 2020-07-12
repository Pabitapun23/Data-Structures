#Implementation of Interpolation Search by Python

def interpolationSearch(arr, n, x):
    #index of two ends
    low = 0
    high = (n-1)

    #elements of sorted array must be in range of two ends
    while low <=  high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        
        pos = low + int(((float(high-low)/(arr[high]-arr[low]))*(x-arr[low])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:    #x is in upper part
            low = pos+1
        else:
            high = pos-1    #x is in lower part
    return -1

arr = [1, 3, 5, 6, 7, 8, 10]
n = len(arr)
x = 7
index = interpolationSearch(arr, n, x)
if index == -1:
    print("Element not found")
else:
    print("The element is found at index ", index)

    
        

    