from math import gcd, isqrt

def pollard_rho(n,  c=1, show=False):
    f = lambda x: (x * x + 5) % n
    a, b, = c, c
    i = 0
    while True:
        i+=1
        a = f(a)
        b = f(f(b))
        d = gcd(abs(a-b), n)
        if show:
            print(f"{i}\t {a}\t {b}\t {d}")
        if d == n:
            return None
        if d > 1:
            return d
    
def fermat_squares(n):
    s = isqrt(n)
    if s * s < n:
        s += 1
    while True:
        t2= s * s - n
        t = isqrt(t2)
        if t * t == t2:
            return s - t, s + t
        s+=1
     
     
def is_prime(n):
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i +=1
    return True

def factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    if n % 2 == 0:
        return [2] + factorize(n // 2)
    r = isqrt(n)
    if r * r == n:
        return sorted(factorize(r) *2)
    
    c = 1
    while True:
        d = pollard_rho(n, c)
        if d:
            return sorted(factorize(d) + factorize(n // d))
        c += 1
        
        
        
# execution
c , n = 1, 1359331

print("i\t a\t b\t d")
d = pollard_rho (n, c, show=True)
print(f"Nontrivial devisor: {d} ---> {n} = {d} * {n//d}")

print(f"\nSquare method on 15: {fermat_squares(15)}")


n = 1359331
print(f"\n{n} =", " * ".join(map(str, factorize(n))))