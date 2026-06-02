def happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        
        for digit in str(n):
            total += int(digit) ** 2
        n = total
    if n == 1:
        return True 
    else:
        return False

num = int(input())

if happy_number(num):
    print("Happy Number")
else:
    print("Not a Happy Number")