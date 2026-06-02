arr = [10, 50, 30, 80, 60]

first=second=third= -9999

for i in arr:

    if i > first:
        third = second
        second = first
        first = i

    elif i > second:
        third = second
        second = i

    elif i > third:
        third = i

print("Third Largest:", third)