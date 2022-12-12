import math

# Exercice 3.5
# Question 1
def fibonacci(n: int) -> int:
    """Préconditions n >= 0"""
    if(n == 0):
        return 0
    f_prev_2: int = 0
    f_prev_1: int = 1
    temp: int = 0
    i: int = 2
    while i <= n:
        temp = f_prev_1
        f_prev_1 = f_prev_2 + f_prev_1
        f_prev_2 = temp
        i = i + 1
    return f_prev_1

assert fibonacci(1) == 1
assert fibonacci(6) == 8

# Question 2
"""
| Boucle | f_prev_2 | f_prev_1 | temp | i |
| Entrée | 0        | 1        | 0    | 2 |
| Tour 1 | 1        | 1        | 1    | 3 |
| Tour 2 | 1        | 2        | 1    | 4 |
| Tour 3 | 2        | 3        | 2    | 5 |
| Tour 4 | 3        | 5        | 3    | 6 |
| Tour 5 | 5        | 8        | 5    | 7 |
| Tour 6 | 8        | 13       | 8    | 8 |
| Sortie | 13       | 21       | 13   | 9 |

"""

def fibo_diff(k: int) -> float:
    """Préconditions k >= 2"""
    return fibonacci(k)/fibonacci(k-1)

assert fibo_diff(2) == 1
assert abs(fibo_diff(5) - 5/3) <= 10**-15
assert abs(fibo_diff(8) - 21/13) <= 10**-15

def fibo_approx(n: int) -> float:
    """Préconditions n >= 0"""
    phi: float = (1 + math.sqrt(5))/2
    return phi**n/math.sqrt(5)

assert round(fibo_approx(5)) == fibonacci(5)
assert round(fibo_approx(10)) == fibonacci(10)
assert round(fibo_approx(20)) == fibonacci(20)

# Exercice 3.6 

def partie_entière(x: float) -> int:
    """Précondition: x >= 0"""
    n: int = 0
    while n <= x:
        n = n + 1
    return n - 1

assert partie_entière(0.66) == 0
assert partie_entière(5.67) == 5

