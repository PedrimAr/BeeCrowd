# Triângulo | bee 1929

import math

a, b, c, d = map(int, input().split())

if math.fabs(b - c) < a < b + c and math.fabs(a - c) < b < a + c and math.fabs(a - b) < c < a + b:
    print('S')

elif math.fabs(c - d) < b < c + d and math.fabs(b - d) < c < b + d and math.fabs(b - c) < d < b + c:
    print('S')

elif math.fabs(b - d) < a < b + d and math.fabs(a - d) < b < a + d and math.fabs(a - b) < d < a + b:
    print('S')

elif math.fabs(c - d) < a < c + d and math.fabs(a - d) < c < a + d and math.fabs(a - c) < d < a + c:
    print('S')

else:
    print('N')
