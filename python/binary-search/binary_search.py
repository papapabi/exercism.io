def binary_search(list_of_numbers, number):
    start, end = 0, len(list_of_numbers) - 1
    return __binary_search(list_of_numbers, number, start, end)


def __binary_search(l, n, start, end):
    if start > end:
        raise ValueError(f'{n} not in list')
    mid = (start + end) // 2
    if n > l[mid]:
        return __binary_search(l, n, mid+1, end)
    elif n < l[mid]:
        return __binary_search(l, n, start, mid-1)
    else:
        return mid
