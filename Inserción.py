def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr3 = [3.4, 2.1, 5.6, 1.2, 4.3]
print("Lista ordenada de decimales:", insertion_sort(arr3))
