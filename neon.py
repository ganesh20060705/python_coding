n = int(input( ))
sq = n * n
s = 0
while sq > 0:
    s += sq % 10
    sq //= 10

if s == n:
    print("Neon Number")
else:
    print("Not a Neon Number")