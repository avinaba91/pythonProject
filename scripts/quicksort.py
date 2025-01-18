def partition(start, end, arr) -> int:
    pivot = arr[end]
    i = start - 1

    for j in range(start,end):
        if arr[j] < pivot:
            i += 1
            swap(i, j, arr)

    swap(i+1, end, arr)
    return i+1

def swap(i,j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def quicksort(start, end, arr):
    if end > start:
        p = partition(start, end, arr)
        quicksort(start, p-1, arr)
        quicksort(p+1, end, arr)

arr = [4,2,7,5,1,6,3]
quicksort(0, len(arr)-1, arr)
print(arr)