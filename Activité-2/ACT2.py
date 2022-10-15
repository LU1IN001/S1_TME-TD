#Wilhem Blondel
import math
import random

def terme_leibniz(n: int) -> float:
    """
    Préconditions n >= 0
    Renvoie le terme n de la somme de leibniz
    """
    return ((-1)**n)/((2*n)+1)

assert terme_leibniz (0) == 1
assert terme_leibniz (1) == -1/3
assert terme_leibniz (10) == 1/21

def somme_leibniz(n: int) -> float:
    """
    Préconditions n >= 0
    Renvoie la somme de leibniz jusqu'à n
    """
    s: float = 0
    i: int = 0
    while(i<=n):
        s = s + terme_leibniz(i)
        i = i + 1
    return s

assert somme_leibniz(0) == 1
assert somme_leibniz(1) == 1-1/3
assert somme_leibniz(4) == 1-1/3+1/5-1/7+1/9

def approx_leibniz(n :int) -> float:
    """
    Préconditions n >= 0
    Renvoie une approximation de pi grâce à la série aleternée de leibniz
    plus n est grand plus pi est précis
    """
    return somme_leibniz(n)*4

assert abs(approx_leibniz(10) - math.pi) < 10**-1
assert abs(approx_leibniz(100) - math.pi) < 10**-2
assert abs(approx_leibniz(1000) - math.pi) < 10**-3

# Suggestion 2

def Mq(q: int) -> float:
    """
    Préconditions q >= 0
    Retourne la valeur de Mq de la formule des frères Chudovsky
    """
    return math.factorial(6*q)/(math.factorial(3*q)*math.factorial(q)**3)

assert abs(Mq(0) - 1) < 10**-10
assert abs(Mq(1) - 120) < 10**-10
assert abs(Mq(3) - 81681600) < 10**-10

def Lq(q: int) -> int:
    """
    Préconditions q >= 0
    Retourne la valeur de Lq de la formule des frères Chudovsky
    """
    return 545140134*q + 13591409

assert Lq(0) == 13591409
assert Lq(1) == 558731543
assert Lq(5) == 2739292079

def Xq(q: int) -> int:
    """
    Préconditions q >= 0
    Retourne la valeur de Xq de la formule des frères Chudovsky
    """
    return (-262537412640768000)**q

assert Xq(0) == 1
assert Xq(1) == -262537412640768000
assert Xq(2) == 262537412640768000**2

def approx_chudnovsky(n: int) -> float:
    """
    Préconditions n >= 0
    Retourne la valeur approximative de pi à partir de la formule des frères Chudovsky
    """
    C: float = 426880 * math.sqrt(10005)
    s: float = 0
    i: int = 0
    while(i<=n):
        s = s + (Mq(i)*Lq(i))/Xq(i)
        i = i + 1
    return C*(1/s)

assert abs(approx_chudnovsky(1)- math.pi) < 10**-15

# Suggestion 3

def approx_chudnovsky_optim(n: int) -> float:
    """
    Préconditions n >= 0
    Retourne la valeur approximative de pi à partir de la formule des frères Chudovsky (Optimisation prise sur https://en.wikipedia.org/wiki/Chudnovsky_algorithm)
    """
    
    C: float = 426880 * math.sqrt(10005)
    s: float = 0
    Mq_var: float = 1.0
    Lq_var: int = 13591409
    Xq_var: int = 1
    i: int = 0
    while(i<=n):
        s = s + (Mq_var*Lq_var)/Xq_var
        Mq_var = Mq_var * (((12*i + 2)*(12*i + 6)*(12*i + 10))/((i+1)**3))
        Lq_var = Lq_var + 545140134
        Xq_var = Xq_var * (-262537412640768000)
        i = i + 1
    return C*(1/s)

# On cherche plus à vérifier si l'optimisation est en accord avec le précédent algorithme
assert abs(approx_chudnovsky_optim(1)- approx_chudnovsky(1)) < 10**-15
assert abs(approx_chudnovsky_optim(5)- approx_chudnovsky(5)) < 10**-15
assert abs(approx_chudnovsky_optim(10)- approx_chudnovsky(10)) < 10**-15
# Suggestion 4


def approx_aleatoire(n: int) -> float:
    """
    Préconditions n > 0
    Retourne la valeur approximative de pi à partir de la loi des grands nombres et donc de l'aléatoire.
    """
    center_x: float = 1/2
    center_y: float = 1/2
    times_in_circle: int = 0
    x: float; y: float

    i: int = 1
    while(i <= n):
        x = random.random()
        y = random.random()

        if((x-center_x)**2 + (y-center_y)**2 <= 1/4):
            times_in_circle = times_in_circle + 1

        i = i + 1

    return (times_in_circle/n)*4

# Suggestion 5

def approx_chudnovsky_optim_2(n: int) -> float:
    """
    Préconditions n >= 0
    Retourne la valeur approximative de pi à partir de la formule des frères Chudovsky (Optimisation prise sur https://en.wikipedia.org/wiki/Chudnovsky_algorithm)
    """
    
    C: float = 426880 * math.sqrt(10005)
    s: float = 0
    Mq_var: float = 1.0
    Lq_var: int = 13591409
    Xq_var: int = 1
    Kq: int = -6
    i: int = 0
    while(i<=n):
        s = s + ((Mq_var*Lq_var)/Xq_var)
        Kq = Kq + 12
        Mq_var = Mq_var * ((Kq**3 - 16*Kq) /((i+1)**3))
        Lq_var = Lq_var + 545140134
        Xq_var = Xq_var * (-262537412640768000)
        i = i + 1
        
    return C*(1/s)

# On cherche plus à vérifier si l'optimisation est en accord avec le précédent algorithme
assert abs(approx_chudnovsky_optim_2(1)- approx_chudnovsky(1)) < 10**-15
assert abs(approx_chudnovsky_optim_2(5)- approx_chudnovsky(5)) < 10**-15
assert abs(approx_chudnovsky_optim_2(10)- approx_chudnovsky(10)) < 10**-15


def approx_borwein_quadratic(n: int) -> float:
    """
    Préconditions: n >= 0
    Retourne une approximation de pi avec l'algorithme de Borwein
    En utilisant l'algorithme de convergence quadratique découverte en 1984
    https://en.wikipedia.org/wiki/Borwein%27s_algorithm
    """
    a: float = math.sqrt(2)
    b: float = 0.0
    p: float = 2 + math.sqrt(2)

    i: int = 1
    while(i<=n):
        b = (1 + b) * math.sqrt(a) / (a + b)
        a = (math.sqrt(a) + (1/math.sqrt(a)))/ 2
        p = ((1+a)*p*b) / (1+b)
        i = i+1
    return p
    
assert abs(approx_borwein_quadratic(1)- math.pi) < 10**-2
assert abs(approx_borwein_quadratic(2)- math.pi) < 10**-4
assert abs(approx_borwein_quadratic(5)- math.pi) < 10**-15

def approx_borwein_nonic(n: int) -> float:
    """
    Préconditions: n >= 0
    Retourne une approximation de pi avec l'algorithme de Borwein
    En utilisant l'algorithme de convergence nonique
    https://en.wikipedia.org/wiki/Borwein%27s_algorithm
    """

    a: float = 1/3
    r: float = (math.sqrt(3) - 1)/2
    s: float = (1 - r**3)**(1/3)
    t: float; u: float; v: float; w: float
    
    i: int = 0
    while(i<n):
        t = 1 + 2*r
        u = (9*r*(1+r+r**2))**(1/3)
        v = t**2 + t*u + u**2
        w = (27*(1 + s + s**2))/v
        a = w*a + 3**(2*i-1) * (1 - w)
        s = ((1 - r)**3)/((t + 2*u)* v)
        r = (1 - s**3)**(1/3)
        i = i + 1
        
    return 1/a

assert abs(approx_borwein_nonic(0) - math.pi) <= 1
assert abs(approx_borwein_nonic(2) - math.pi) <= 10**-15

def approx_gauss(n: int) -> float:
    """
    Préconditions: n >= 0
    Retourne une approximation de pi avec l'algorithme de Gauss
    https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm
    """

    a: float = 1.0
    a_prev: float = a
    b: float = 1/math.sqrt(2)
    t: float = 1/4
    p: int = 1
    
    i: int = 0
    while(i<n):
        a = (a + b)/2
        b = math.sqrt(a_prev*b)
        t = t - p*(a_prev-a)**2
        a_prev = a
        p = 2*p
        i = i + 1

    return ((a + b)**2)/(4*t)

# Jeu de test basé sur les données de la page Wikipédia
assert abs(approx_gauss(1) - 3.140) <= 10**-3
assert abs(approx_gauss(2) - 3.14159264) <= 10**-8
assert abs(approx_gauss(3) - math.pi) <= 10**-15
