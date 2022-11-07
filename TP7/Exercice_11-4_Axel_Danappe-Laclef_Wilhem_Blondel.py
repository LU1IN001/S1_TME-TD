#Question 1
import math
def f_fun(x : float) -> float :
    """Retourne la fonction selon le x choisi"""
    return x**2 - 2

assert f_fun(2) == 2

def f_deriv(x : float) -> float :
    """Retourne la fonction dérivée de f selon le x choisi"""
    return 2 * x

assert f_deriv(2) == 4


#Question 2
def approx_newton(f : Callable[[float], float], df : Callable[[float], float], x0 : float, n : int) -> float :
    """Retourne le n-ième terme de la suite"""
    if n == 0 :
        return x0
    else :
        xn: float = x0 - f(x0)/df(x0)
        return approx_newton(f, df, xn, n-1)


assert abs(approx_newton(f_fun, f_deriv, 1.0, 2) - 1.4166666666666667) <= 10**-15
assert abs(approx_newton(f_fun, f_deriv, 1.0, 5) - math.sqrt(2)) <= 10**-15

#Question 3
def approx_newton_it(f : Callable[[float], float], df : Callable[[float], float], x0 : float, n : int) -> float :
    """Retourne le n-ième terme de la suite"""
    y : float = x0
    i : int
    for i in range(n) :
        y = y - f(y)/df(y)
    return y

assert abs(approx_newton_it(f_fun, f_deriv, 1.0, 2) - 1.4166666666666667) <= 10**-15
assert abs(approx_newton_it(f_fun, f_deriv, 1.0, 5) - math.sqrt(2)) <= 10**-15


#Question 4
def g_fun(x : float) -> float :
    """Retourne la fonction selon le x choisi"""
    return math.cos(x) - x**3

assert abs(g_fun(0.0) - 1.0) <= 10**-15

def g_deriv(x : float) -> float :
    """Retourne la fonction dérivée de f selon le x choisi"""
    return -math.sin(x) - 3*x**2

assert abs(g_deriv(1.0) + 3.8414709848078967) <= 10**-15

def resolution(n : int) -> float :
    """Retourne le n-ième terme de la suite suivant l'énoncé"""
    return approx_newton(g_fun, g_deriv, 0.5, n)

assert abs(resolution(2) - 0.9096726937368068) <= 10**-15
