def findDuplicate(arr):
    # Phase 1: Find intersection point
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Phase 2: Find entrance to cycle (duplicate number)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow


print("Test Case 1:", findDuplicate([1, 3, 4, 2, 2]))
