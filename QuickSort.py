#Implementation of Quick Sort by Python

#function that divides
def divideFunc(arr, low, high):
    i = (low-1)
    pivot = arr[high]  #here pivot mns pivot element
    for j in range(low, high):
        if arr[j] <= pivot:  #current element is smaller
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

#for sorting
def quick_sort(arr, low, high):
    if low<high:
        d = divideFunc(arr, low, high)
        quick_sort(arr, low, d-1)
        quick_sort(arr, d+1, high)

#main func
arr = [4, 1, 7, 3, 10, 6, 9]
n = len(arr)
quick_sort(arr, 0, n-1)
for i in range(n):
    print(arr[i], end=" ")




