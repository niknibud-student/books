def sum_arr(lst: list) -> int:
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum_arr(lst[1:])

arr = [1, 2, 3, 4]

print(sum_arr(arr))

def len_arr(lst: list) -> int:
    if len(lst) == 1:
        return 1
    return 1 + len_arr(lst[1:])

print(len_arr(arr))

def max_arr(max_item: int, lst: list) -> int:
    if len(lst) == 1:
        return lst[0]    
    return max_item if max_arr(max_item, lst[1:]) < max_item else max_arr(max_item, lst[1:])
    
print(max_arr(arr[0], arr[1:]))

def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 5, 2, 3]))