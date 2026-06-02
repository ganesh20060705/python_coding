def binary( arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
target = int(input())
result = binary(arr, target)
if result != -1:
    print("card valid")
else:
    print("not valid")