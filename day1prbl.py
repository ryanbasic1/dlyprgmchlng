def solution(array):
    count0 = count1 = count2 = 0
    
    # Count no. of times the 0 1 2
    for num in array:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    i = 0
    for _ in range(count0):
        array[i] = 0
        i += 1
    for _ in range(count1):
        array[i] = 1
        i += 1
    for _ in range(count2):
        array[i] = 2
        i += 1
    
    return array

arr =  [0, 1, 2, 1, 0, 2, 1, 0]
print(solution(arr))
