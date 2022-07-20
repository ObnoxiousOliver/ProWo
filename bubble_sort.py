def bubble_sort (arr, compare_func = lambda a, b: a > b):
    l = len(arr)

    for i in range(l - 1):
        for j in range(l - 1 - i):
            if compare_func(arr[j], arr[j + 1]):
                # Swap!
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

inp = input('Enter an array of numbers (seperate with ","): ')
# split string and parse numbers
arr = list(map(lambda x: int(x), inp.split(',')))
print(bubble_sort(arr))
