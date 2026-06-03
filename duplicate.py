s = input("Enter string: ")

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

print("Duplicate characters:")

for ch in count:
    if count[ch] > 1:
        print(ch)