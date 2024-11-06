def bubble_sort_strings_by_length(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr2 = ["casa", "perro", "a", "elefante", "gato"]
print("Lista ordenada por longitud:", bubble_sort_strings_by_length(arr2))
