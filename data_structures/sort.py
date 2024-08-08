def insertion_sort(array, lambda_=None):
    n = len(array)
    for j in range(1, n):
        i = j
        key = array[i]
        while i > 0 and lambda_(key) < lambda_(array[i - 1]):
            array[i] = array[i - 1]
            i -= 1
        array[i] = key
    return array
