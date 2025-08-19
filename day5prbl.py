def leaders(arr):
    n = len(arr)
    if n == 0:
        return []
    res = []
    max_so_far = float('-inf')
    for x in reversed(arr):
        if x > max_so_far:
            res.append(x)
            max_so_far = x
    return res[::-1]

arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))