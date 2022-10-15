import math

def volume_tetraedre(a: float, b: float, c: float, d: float, e: float, f: float) -> float:
    """
    Precondition a,b,c,d,e,f > 0
    retourne le volume du tétraèdre d'après Leonhard Euler
    """
    x: float = a**2 + b**2 - d**2
    y: float = b**2 + c**2 - e**2
    z: float = a**2 + c**2 - f**2
    p: float = 4* a**2 * b**2 * c**2
    q: float = a**2 * y**2 + b**2 * z**2 + c**2 * x**2
    r: float = x * y * z
    return 1/12*math.sqrt(p-q+r)

assert abs((volume_tetraedre(1,1,1,1,1,1) - 0.11785113019775792)) <= 10**-15
assert abs((volume_tetraedre(2,2,2,2,2,2) - 0.9428090415820634)) <= 10**-15
# Question subisidaire
assert abs(volume_tetraedre(4, 2, 5, math.sqrt(20), math.sqrt(29), math.sqrt(41)) - 20/3) <= 10**-15

# Question 2

def volume_tetraedre_regulier(a: float) -> float:
    """
    Precondition a > 0
    retourne le volume du tétraèdre régulier d'après Leonhard Euler
    """
    return volume_tetraedre(a,a,a,a,a,a)


assert abs((volume_tetraedre_regulier(1) - 0.11785113019775792)) <= 10**-16
assert abs((volume_tetraedre_regulier(2) - 0.9428090415820634)) <= 10**-16
