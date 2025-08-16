# def solution(n):
#     output = []
#     if len(n) ==1:
#         for i in range((n[0])):
#             if i not in n:
#                 output.append(i)
#         return output
#     for i in range(1,len(n)+2):
#         if i not in n:
#             return i
        

# arr = [1,2,3]

# print(solution(arr))

def solution(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)

arr = [1, 2, 3, 4]
print(solution(arr)) 