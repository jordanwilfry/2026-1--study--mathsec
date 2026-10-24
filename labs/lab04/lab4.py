# Алгоритм Евклида.
def euclid(a, b):
    while b != 0:
        a, b = b , a%b
    return a

# Бинарный алгоритм Евклида.
def binary_euclid(a, b):
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a //= 2
        b //= 2
        g *= 2
    u, v = a, b
    while u != 0:
        while u % 2 == 0:
            u //= 2
        while v % 2 == 0:
            v //= 2
        if u >= v:
            u = u-v
        else:
            v = v-u
    return g * v


# Расширенный алгоритм Евклида.
def extended_euclid(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a , x0, y0

# Расширенный бинарный алгоритм Евклида.
def binary_extended_euclid(a, b):
    a0, b0 = a, b
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a //= 2
        b //= 2
        g *= 2
    u , v = a, b
    A, B, C, D = 1, 0, 0, 1
    while u != 0:
        while u % 2 == 0:
            u //= 2
            if A % 2 == 0 and B % 2 == 0:
                A //= 2
                B //= 2
            else:
                A = (A + b) // 2
                B = (B - a) // 2
        while v % 2 == 0:
            v //= 2
            if C % 2 == 0 and D % 2 == 0:
                C //= 2
                D //= 2
            else:
                C = (C + b) // 2
                D = (D - a) // 2
        if u >= v:
            u -= v
            A -= C
            B -= D
        else:
            v -=u
            C -=A
            D -= B
    return g * v, C, D


tests = [(24690, 12345), (54321, 12345), (12541, 12345)]

for a, b in tests:
    print(f"a = {a}, b = {b}")
    
    print("\nЕвклид:", euclid(a, b))
    
    print("\nБинарный Евклид:", binary_euclid(a, b))
    print("\nРасширенный Евклид:", extended_euclid(a, b))
    print("\nБинарный расширенный Евклид:", binary_extended_euclid(a, b))
    print()

