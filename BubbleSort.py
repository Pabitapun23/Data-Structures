#Implementation of Bubble Sort by Python

def bubble_sort(arr):
    n = len(arr)
    for passingNum in range(n-1, 0, -1):
        for i in range(passingNum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

arr = [2, 4, 1, 19, 3, 39, 30, 25]
bubble_sort(arr)
print(arr)