def insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr4 = ["uva", "manzana", "pera", "naranja", "kiwi"]
print("Lista ordenada alfabéticamente:", insertion_sort_strings(arr4))
