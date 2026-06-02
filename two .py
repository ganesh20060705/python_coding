def two_sum(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False


n = int(input())
arr = list(map(int, input().split()))   
target = int(input())
if two_sum(arr, target):
    print("Element Found")
else:
    print("Element Not Found")

    