def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
            else:
                break


A = [2, 8, 5, 3, 9, 1, 4, 2, 8, 5, 3, 9, 4]
insertionSort(A)
print(A)
