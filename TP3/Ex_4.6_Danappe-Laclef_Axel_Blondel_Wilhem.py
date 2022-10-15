#Exercice 4.6 : Combinaisons
#Question 1
def factorielle(n : int) -> int:
    """Précondition : n >= 0
    Retourne le produit factoriel n!
    """
    k : int = 1
    f : int = 1
    nb_ops : int = 0
    while k <= n:
        f = f * k
        k = k + 1
        nb_ops = nb_ops +1
    print("Nombre d'opérations =",nb_ops)
    return f
assert factorielle(5) == 120
assert factorielle(6) == 720

#Question 2
def combinaisons(n : int, k : int) -> float:
    """Précondition : n >= k and n>=0 and k>=0
    Retourne la combinaison de k parmi n"""
    return (factorielle(n))/(factorielle(k)*(factorielle(n-k)))

#Question 3
# il faut 5+2+3=10 multiplication pour calculer combinaisons(5,2)
# il faut 10+4+6=20 multiplication pour calculer combinaisons(10,4)
# il faut 1000+2+998=2000 multiplication pour calculer combinaisons(1000,2)
# il faut 10000+450+9550=20000 multiplication pour calculer combinaisons(10000,450)

#Question 4
def combis_rapide(n: int,k: int) -> float:
    """Précondition : n >= k and n>=0 and k>=0
    Retourne la combinaison de k parmi n"""
    i: int = 1
    p: float = 1.0
    while(i<=k):
        p = p * (n+1-i)/i
        i = i+1
    return p


# Question 5
"""

| Boucle | p   | i |
| Entrée | 1   | 1 |
| Tour 1 | 10  | 2 |
| Tour 2 | 45  | 3 |
| Tour 3 | 120 | 4 |
| Sortie | 210 | 5 |

| Boucle | p      | i |
| Entrée | 1      | 1 |
| Tour 1 | 1000   | 2 |
| Sortie | 499500 | 3 |
"""
