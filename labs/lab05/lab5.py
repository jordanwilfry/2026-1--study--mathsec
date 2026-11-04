import random

# 1. Алгоритм, реализующий тест Ферма.
def fermat_test(n):
    a = random.randint(2, n-2)
    r = pow(a, n - 1, n)
    if r == 1:
        return "вероятно, простое"
    return "составное"



# 2. Алгоритм вычисления символа Якоби.
def jacobi(a, n):
    g = 1
    while True:
        if a == 0:
            return 0
        if a == 1:
            return g
        
        k = 0
        a1= a
        while a1 % 2 == 0:
            a1 //= 2
            k += 1
        
        if k % 2 == 0:
            s=1
        elif n%8 in (1, 7):
            s=1
        else:
            s=-1

        if a1 == 1:
            return g* s
        
        if n % 4 == 3 and a1 % 4 == 3:
            s= -s
        
        a= n% a1
        n=a1
        g = g* s




# 3. Алгоритм, реализующий тест Соловэя-Штрассена.
def solovay_strassen_test(n):
    a = random.randint(2, n-2)
    r = pow(a, (n-1)//2, n)
    if r != 1 and r != n-1:
        return "составное"
    s = jacobi(a, n)
    if r != s % n:
        return "составное"
    return "вероятно, простое"




# 4. Алгоритм, реализующий тест Миллера-Рабина.
def miller_rabin_test(n):
    s= 0
    r= n-1
    while r % 2 == 0:
        r //= 2
        s+= 1
    
    a = random.randint(2, n-2)
    y= pow(a, r, n)

    if y != 1 and y != n-1:
        j=1
        while j <= s-1 and y != n-1:
            y = (y*y) %n
            if y == 1:
                return "составное"
            j+=1
        if y != n-1:
            return "составное"
        
    return "вероятно, простое"


def repeat_test(test, n, t=10):
    for _ in range(t):
        if test(n) == "составное":
            return "составное"
    return "вероятно, простое"


print(f"Jacobi (5, 21) = {jacobi(5, 21)}")
print(f"Jacobi (3, 7) = {jacobi(3, 7)}")
print(f"Jacobi (2, 7) = {jacobi(2, 7)}")
print()


# primes: 97, 7919, 104729. composites: 91, 561, 1001
for n in [97, 7919, 104729, 91, 561, 1001]:
    print(f"n = {n}")
    print(f"  Fermat:    {repeat_test(fermat_test, n)}")
    print(f"  Solovay_Strassen:    {repeat_test(solovay_strassen_test, n)}")
    print(f"  Miller-Rabin:    {repeat_test(miller_rabin_test, n)}")
    print("\n//////////////////////\n")