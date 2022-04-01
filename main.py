


arr = [1,4,2]
def insertSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while (i>=0 and arr[i] > key):
            arr[i+1] = arr[i]
            i = i -1
        arr[i+1] = key
    return arr

print(insertSort(arr))