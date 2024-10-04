# bee 1103 | Alarme Despertador

while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == m1 == h2 == m2 == 0:
        break
    
    h1 = h1 * 60 + m1
    h2 = h2 * 60 + m2
    
    if h1 >= h2:
        h2 += 1440

    print(abs(h2 - h1))
