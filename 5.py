n = int(input())
arr = list(map(int, input().split()))
target = int(input())

if target in arr:
    print("Element Found")
else:
    print("Element Not Found")