
def find_pairs(arr, target_sum):
    pairs = set()
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)

    return list(pairs)

arr = [2, 4, 5, 3, 6, 8]
target_sum = 10
print(find_pairs(arr, target_sum))

