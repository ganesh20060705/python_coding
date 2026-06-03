s = input("Enter string: ")

result = ""

for ch in s:
    if ch.isalnum():
        result += ch

print(result)