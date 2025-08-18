import math

def merge_sorted_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    total_length = m + n
    gap = math.ceil(total_length / 2)

    while gap > 0:
        i = 0
        j = gap
        while j < total_length:
            if i < m:
                first = arr1[i]
            else:
                first = arr2[i - m]

            if j < m:
                second = arr1[j]
            else:
                second = arr2[j - m]

            if first > second:
                if i < m and j < m:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                elif i < m and j >= m:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]
                else:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        if gap == 1:
            break
        gap = math.ceil(gap / 2)

    return arr1 + arr2
# Example usage
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2))