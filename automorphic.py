n = int(input())
square = n * n
digits = len(str(n))
if square % (10 ** digits) == n:
    print("Automorphic ")
else:
    print("Not  Automorphic ")