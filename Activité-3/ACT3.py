# Wilhem Blondel
import math
def divise(k: int, n: int) -> bool:
    """Pre : k > 0 and n >= 0
    Decide si k divise n """
    return n % k == 0

def est_parfait(n: int) -> bool:
    """Pre: n >= 1
    Decide si n est un nombre parfait"""
    s: int = 0
    i: int = 1
    while i != n:
        if divise(i,n):
            s = s + i
        i = i + 1
    return n == s

# Jeu de test

assert divise(12, 48) == True
assert divise(11, 253) == True
assert divise(3, 56) == False
assert divise(3, 49) == False

assert est_parfait(6) == True
assert est_parfait(8128) == True
assert est_parfait(5) == False
assert est_parfait(1000) == False

def est_parfait_simulee(n: int) -> bool:
    """Pre: n >= 1
    Decide si n est un nombre parfait"""
    s: int = 0
    i: int = 1
    print("début de la boucle, s =", s)
    print("début de la boucle, i =", i)
    print("==========================")
    while i != n:
        if divise(i,n):
            s = s + i
        i = i + 1
        print("fin du tour",i-1, "s =", s)
        print("fin du tour",i-1, "i =", i)
        print("==========================")
    print("sortie de boucle, s =", s, "n =", n)
    return n == s

# Suggestion 2

def test_parfait(n: int) -> bool:
    """
    Préconditions: n >= 1 et n <= 137 438 691 328
    Vérifie si est_parfait renvoie des résultats valide jusqu'à n
    """
    k: int = 1
    while k <= n:
        if(k == 6 or k == 28 or k == 496 or k == 8128 or k == 33550336 or k == 8589869056 or k == 137438691328):
            if not est_parfait(k):
                return False
        elif est_parfait(k):
            return False
        k = k + 1
    return True

assert test_parfait(496) == True

# Suggestion 3

def invariant(i: int, n: int, s: int) -> bool:
    """
    Indique si l'invariant de est_parfait est vrai ou faux
    """
    somme: int = 0
    j: int = 1
    while j <= i - 1:
        if n%j == 0:
            somme = somme + j
        j = j + 1
    return s == somme

def est_parfait_invariant(n: int) -> bool:
    """Pre: n >= 1
    Decide si n est un nombre parfait"""
    s: int = 0
    i: int = 1
    if(invariant(i,n,s)):
        print("Invariant vrai")
    else:
        print("Invariant faux")
    while i != n:
        if divise(i,n):
            s = s + i
        i = i + 1
        if(invariant(i,n,s)):
            print("Invariant vrai")
        else:
            print("Invariant faux")
    if(invariant(i,n,s)):
        print("Invariant vrai")
    else:
        print("Invariant faux")
    return n == s

# Suggestion 4
# Question 1
def est_parfait_fichier(n: int) -> bool:
    """Pre: n >= 1
    Decide si n est un nombre parfait
    Génère un fichier avec un tableau de simulation"""
    with open("/Users/wilhe/Desktop/Sorbonne Workspace/PPTI-Retrieved/Activité-3/simulation_act3_sugg4_q1.txt", 'w') as fichier :
        s: int = 0
        i: int = 1
        fichier.write("début de la boucle, s = "+str(s)+"\n")
        fichier.write("début de la boucle, i = "+str(i)+"\n")
        fichier.write("==========================\n")
        while i != n:
            if divise(i,n):
                s = s + i
            i = i + 1
            fichier.write("fin du tour" + str(i-1) + " s = "+ str(s)+"\n")
            fichier.write("fin du tour" + str(i-1) + " i =" + str(i)+"\n")
            fichier.write("==========================\n")
        fichier.write("sortie de boucle, s = " + str(s) + " n = "+ str(n)+"\n")
        return n == s

# Suggestion 5

# Question 1
def est_parfait_appels(n: int) -> bool:
    """Pre: n >= 1
    Decide si n est un nombre parfait"""
    s: int = 0
    i: int = 1
    times: int = 0
    while i != n:
        times = times + 1
        if divise(i,n):
            s = s + i
        i = i + 1
    print(times, "appels a la fonction divise.")
    return n == s

# Question 2
def est_parfait_opti_appels(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait """
    s : int = 1
    i : int = 2
    times: int = 0
    if i == 1:
        return False
    while i != int(math.sqrt(n)) + 1 :
        times = times + 1
        if divise(i, n):
            if i != math.sqrt(n) :
                s = s + i + (n // i)
            else :
                s = s + i
        i = i + 1
    print(times, "appels a la fonction divise.")
    return n == s

# Question 3

# est_parfait(n) appel n-1 fois la fonction divise
# est_parfait_opti(n) semble appeler log(n) fois la fonction divise


# Question 4
def est_parfait_graphe(n: int) -> bool:
    """Pre: n >= 1
    Decide si n est un nombre parfait"""
    s: int = 0
    i: int = 1
    times: int = 0
    k: int = 1
    overlay_to_show: Image = draw_line(-1, -1, -1, -1)
    x_prev: float = -1
    y_prev: float = -1
    while k <= n:
        while i != k:
            times = times + 1
            if divise(i,k):
                s = s + i
            i = i + 1
        overlay_to_show = overlay(overlay_to_show, draw_line(x_prev, y_prev, -1+2*i/n, -1+2*times/n))
        x_prev = -1+2*i/n
        y_prev = -1+2*times/n
        k = k + 1
    
    # ---- Opti ----
    
    k = 1
    x_prev = -1
    y_prev = -1
    while k <= n:
        s = 1
        i = 2
        times = 0
        while(i != int(math.sqrt(k)) + 1):
            times = times + 1
            if divise(i, k):
                if i != math.sqrt(k) :
                    s = s + i + (k // i)
                else :
                    s = s + i
            i = i + 1
        overlay_to_show = overlay(overlay_to_show, draw_line(x_prev, y_prev, -1+2*k/n, -1+2*times/n))
        x_prev = -1+2*k/n
        y_prev = -1+2*times/n
        k = k + 1
    

    show_image(overlay_to_show)
    return n == s
    
