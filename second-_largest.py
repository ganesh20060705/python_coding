def find_second_largest(arr):
    first = second = -9999

    for i in arr:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i

    return second   
n=int(input())    
arr = []
for i in range(n):
    arr.append(int(input()))
s_largest = find_second_largest(arr)