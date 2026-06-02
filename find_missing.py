arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))

total = n * (n + 1) // 2

arr_sum = sum(arr)

missing = total - arr_sum

print("Missing Element:", missing)