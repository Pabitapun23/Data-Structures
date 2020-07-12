#Implementation of Binary Search by Python

#for sorting
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = binarySearch(arr, temp, 0, i) + 1
        for k in range(i, pos, -1):
            arr[k] = arr[k-1]
        arr[pos] = temp

def binarySearch(arr, key, start, end):
    if end - start <= 1:
        if key < arr[start]:
            return start-1
        else:
            return start
    mid = (start + end)//2

    if arr[mid] < key:
        return binarySearch(arr, key, mid, end)
    elif arr[mid] > key:
        return binarySearch(arr, key, start, mid)
    else:
        return mid

arr = [1, 3, 25, 20, 4, 9]
insertionSort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")


