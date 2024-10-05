# bee 2342 | Overflow

n = int(input())
p, c, q = input().split()
p, q = int(p), int(q)

if c == "+":
    resultado = p + q
else:
    resultado = p * q

if resultado > n:
    print("OVERFLOW")
else:
    print("OK")
