def find_lis(arr):
    if not arr:
        return []

    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    max_index = lis.index(max_length)

    result = [arr[max_index]]
    current_length = max_length
    for i in range(max_index - 1, -1, -1):
        if arr[i] < arr[max_index] and lis[i] == current_length - 1:
            result.insert(0, arr[i])
            current_length -= 1

    return result


arr = [3, 10, 2, 1, 20]
print(find_lis(arr))  # Выведет [3, 10, 20]