#Implementation of Insertion Sort by Python

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        #move elements of arr[0, 1, ... i-1] that are greater than the key to the one place ahead of their current place

        j = i-1

        while key < arr[j] and j>=0:
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = key

arr = [5, 2, 6, 89, 293, 33]
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i])
