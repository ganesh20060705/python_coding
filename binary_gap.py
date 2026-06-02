n = int(input())

b = bin(n)[2:]

pos = []

for i in range(len(b)):
    if b[i] == '1':
        pos.append(i)

max_gap = 0

for i in range(1, len(pos)):
    max_gap = max(max_gap, pos[i] - pos[i-1])

print(max_gap)