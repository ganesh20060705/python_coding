n = input()
s = 0

for i in range(len(n)):
    s += (i + 1) * int(n[i])

if s % 11 == 0:
    print("Valid ISBN")
else:
    print("Invalid ISBN")
