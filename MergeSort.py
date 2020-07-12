#Implementation of Merge Sort by Python

def merge_sort(arr):
    n = len(arr)
    if n>1:
        mid = n//2 #mid point of array

        #Divide elements of array in two halves
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k = k + 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1
    print("Merging the array", arr)

arr = [10, 23, 13, 5, 39, 25, 15]
merge_sort(arr)
print(arr)

    