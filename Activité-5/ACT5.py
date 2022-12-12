# Wilhem Blondel
Polyn = List[int]

ex1 : Polyn = [3, 0, 2]
ex2 : Polyn = [1, -1, 1, -1, 0]
ex3 : Polyn = [27]
ex4 : Polyn = []

def degre(polynome: Polyn) -> int:
    """Retourne le degré du polynôme"""
    i: int
    for i in range(len(polynome)-1, -1, -1):
        if(polynome[i] != 0):
            return i
    return 0

assert degre(ex1) == 2
assert degre(ex2) == 3
assert degre(ex3) == 0
assert degre(ex4) == 0
assert degre([0,0,0,0,0]) == 0


def somme(p1: Polyn, p2: Polyn) -> Polyn:
    """Retourne la somme des polynômes donnés"""
    pres: Polyn = []
    p1_len: int = len(p1)
    p2_len: int = len(p2)
    i: int
    for i in range(max(p1_len,p2_len)):
        if(i >= p2_len):
            pres.append(p1[i])
        elif(i >= p1_len):
            pres.append(p2[i])
        else:
            pres.append(p1[i] + p2[i])
    return pres

assert somme(ex1, ex1) == [6, 0, 4]
assert somme(ex1, ex4) == ex1
assert somme(ex1, ex2) == [4, -1, 3, -1, 0]

def normalise(p: Polyn) -> Polyn:
    """Retire tous les termes nulle d'un polynôme qui ne servent à rien"""
    i: int
    for i in range(len(p)-1, -1, -1):
        if(p[i] != 0):
            return p[:i+1]
    return []

assert normalise(ex1) == ex1
assert normalise(ex2) == [1, -1, 1, -1]
assert normalise([0, 0, 0, 0, 0]) == []
assert normalise([]) == []


def produit(p1: Polyn, p2: Polyn) -> Polyn:
    """Retourne le produit des polynômes p1 et p2"""
    i: int
    j: int
    k: int
    l: int
    m: int
    pres: Polyn = []
    d_1: int = degre(p1)
    d_2: int  = degre(p2)
    if(p1 == [] or p2 == []):
        # C'est un cas particulier inintéressant car on multiplie par 0
        # Afin d'éviter de vérifier des index qui n'existent pas
        # On return immédiatemment une liste vide
        return []
    for j in range(d_1 + d_2 + 1):
        # Initialisation de la liste à modifier
        # On modifie les index à l'envers, d'où l'intérêt de créer une
        # liste au préalable pour pouvoir évaluer les plus haut index
        pres.append(0)
    if(d_1 >= d_2):
        for i in range(d_1 + 1):
            for k in range(d_2 + 1):
                pres[d_1+d_2-k-i] = pres[d_1+d_2-k-i] + p1[d_1-i] * p2[d_2-k]
        return pres
    else:
        for l in range(d_2 + 1):
            for m in range(d_1 + 1):
                pres[d_1+d_2-l-m] = pres[d_1+d_2-l-m] + p1[d_1-m] * p2[d_2-l]
        return pres


assert normalise(produit(ex1, ex4)) == []
assert normalise(produit(ex1, ex1)) == [9, 0, 12, 0, 4]
assert normalise(produit(ex1, ex2)) == [3, -3, 5, -5, 2, -2]
assert normalise(produit(ex1, ex3)) == [27* 3, 0, 27* 2]
assert normalise(produit([1, 1], [1, 0, 1])) == [1, 1, 1, 1]

# Suggestion 2

def multiplication_polynome(p1: Polyn, coef: int) -> Polyn:
    """Retourne le polynôme multiplié par l'entier donné"""
    pres: Polyn = p1[:]
    i: int
    for i in range(len(pres)):
        pres[i] = pres[i]*coef
    return pres

assert normalise(multiplication_polynome(ex1, 2)) == [6, 0, 4]
assert normalise(multiplication_polynome(ex4, 10)) == []
assert normalise(multiplication_polynome(ex3, -1)) == [-27]


def puissance_polyn(p1: Polyn, power: int) -> Polyn:
    """Préconditions: power >= 0
    Retourne le polynôme élevé à la puissance donnée"""
    if(power == 0):
        return [1]
    pres: Polyn = p1[:]
    i: int
    for i in range(1, power):
        pres = normalise(produit(pres, p1))
    return pres

assert normalise(puissance_polyn(ex1, 2)) == normalise(produit(ex1, ex1))
assert normalise(puissance_polyn(ex4, 0)) == [1]
assert normalise(puissance_polyn(ex4, 6)) == []
assert normalise(puissance_polyn(ex3, 5)) == [27**5]

def derivee(p1: Polyn) -> Polyn:
    """Retourne la dérivation du polynôme"""
    pres: Polyn = []
    x_power: int = 1
    i: int
    for i in p1[1:]:
        pres.append(x_power*i)
        x_power = x_power + 1
    return pres

assert normalise(derivee(ex1)) == [0, 4]
assert normalise(derivee(ex4)) == []
assert normalise(derivee(ex2)) == [-1, 2, -3]

def primitive(p1: Polyn, k: int = 0) -> Polyn:
    """Préconditions, les coefficients doivent se diviser avec les puissances supérieures
    Retourne la primitive du polynôme donné avec une constante au choix k
    Par défaut k = 0"""
    pres: Polyn = [k]
    x_power: int = 1
    i: int
    for i in p1:
        pres.append(i//x_power)
        x_power = x_power + 1
    return pres

assert normalise(primitive(derivee(ex1), 3)) == normalise(ex1)
assert normalise(primitive(derivee(ex2), 1)) == normalise(ex2)
assert normalise(primitive(derivee(ex3), 27)) == normalise(ex3)
assert normalise(primitive(derivee(ex4), 12)) ==  [12]


# Suggestion 3

def valeur(p1: Polyn, x: float) -> float:
    """Retourne le résultat du polynôme de x"""
    i: int
    res: float = 0.0
    for i in range(len(p1)):
        res = res + p1[i]*x**i
    return res

assert valeur(ex1, 0) == 3
assert valeur(ex1, -1) == 5
assert valeur(ex4, 2.5) == 0


def courbe_poly(p: Polyn, nx: int, ny: int) -> Image:
    """Renvoie le dessin de la courbe p entre les points (-nx, -ny) et (nx, ny)"""
    x_prev: float = -1
    y_prev: float = valeur(p, -nx)/ny
    curve: Image = draw_line(x_prev, y_prev, x_prev, y_prev)
    i: float = -nx + 0.01 # 0.01 représente la précision, plus elle ets basse plus la courbe sera précise
    while i < nx+nx/ny:
        x_to_test: float = i/nx # Récupère la valeur de x adapaté au graphe [-1, 1]
        y_obtained: float = valeur(p, i)/ny # Récupère la valeur de y adapaté au graphe [-1, 1]
        join: Image = draw_line(x_prev, y_prev, x_to_test, y_obtained)
        curve = overlay(curve, join)
        x_prev = x_to_test
        y_prev = y_obtained
        i = i + 0.01 # i représente en réalité le x que l'on remplace dans le polynôme
    return curve

#show_image(courbe_poly(ex2, 10, 100))


# Suggestion 4

def cdp(p: Polyn) -> str:
    """Retourne la structure du polynôme sous la forme d'un str lisible"""
    # On vérifie le cas particulier de la liste vide
    if(len(p) == 0):
        return "0"
    res: str =  ""
    sign: str = "" # Chaîne contenant le signe du coefficient
    num: str = "" # Chaîne contenant le coefficient
    x_multiplied: str = "" # Chaîne de caractère contenant la puissance de X adéquate
    i: int
    for i in range(degre(p)+1):

        # ----- Gestion du X -----
        if i==1:
            x_multiplied = "X" # Dégré 1
        elif i > 1:
            x_multiplied = "X^"+str(i) # Dégré i

            
        # ----- Gestion du coefficient -----
        if(abs(p[i]) <= 1):
            num = "" # Le coeffcient est nul ou égal à 1
            if(abs(p[i]) == 1 and i == 0):
                num = str(abs(p[i]))
            # Si le dégré est 0 il faut que le coefficient s'affiche même s'il vaut 1 mais pas 0
        else:
            if(x_multiplied == ""):
                # Il n'y a pas de X qui multiplie le coefficient
                # On n'ajoute pas de .
                num = str(abs(p[i]))
            else:
                num = str(abs(p[i])) + "."

        # ----- Gestion du signe -----
        if(p[i] < 0):
            sign = "-"
        elif(p[i] > 0):
            sign = ""
            if(i != degre(p)):
                sign = "+"
        else:
            sign = ""
            x_multiplied = ""

        # ----- Gestion des espaces -----

        if(i == degre(p)):
            res = sign + num + x_multiplied + res
        elif(sign + num + x_multiplied != ""):
            res = " " + sign + " " + num + x_multiplied + res

    return res

assert cdp(ex1) == "2.X^2 + 3"
assert cdp(ex4) == "0"
assert cdp(ex2) == "-X^3 + X^2 - X + 1"
assert cdp(ex3) == "27"
assert cdp(produit(ex1, ex2)) == "-2.X^5 + 2.X^4 - 5.X^3 + 5.X^2 - 3.X + 3"

def pdc(p: str) -> Polyn:
    """Préconditions: Respecter la structure du polynôme en str
    Converti un polynôme str vers une liste Polyn"""
    pres: Polyn = []
    coef: str = ""
    power: str = ""
    prev_power: int = -1
    waiting_for_coef: bool = True
    has_power: bool = False
    ignore_next_space: bool = False
    i: int
    for i in range(len(p)):
        if(p[i] == " " and not ignore_next_space):
            # On a terminé de récupérer un terme
            if not has_power:
                # Si on a pas trouvé de "^"
                # Alors la puissance vaut 1 si on est encore dans la boucle
                power = "1"
            if(coef == "" or coef == "+"):
                # Si le coefficient n'a pas de chiffre
                # Alors c'est forcément 1
                coef = "1"
            elif(coef == "-"):
                # Si on a un ciefficient qui ne contient que le signe négatif
                # Alors il vaut forcément - 1
                coef = "-1"
            if(prev_power == -1):
                # On a la puissance la plus haute
                if(int(coef) != 0):
                    pres.append(int(coef))
                prev_power: int = int(power)
            else:
                j: int
                for j in range(prev_power-int(power)-1):
                    # On ajoute autant de 0 que de différence entre les puissances
                    pres.append(0)
                if(int(coef) != 0):
                    pres.append(int(coef))
                prev_power: int = int(power)

            # Réinitialisation des variables
            coef = ""
            power = ""
            ignore_next_space = True
            waiting_for_coef = True
            has_power = False
            
        elif(p[i] == " " and ignore_next_space):
            # C'est l'espace après l'opérateur, on l'ignore
            # Le prochain espace permettra de délimiter le terme
            ignore_next_space = False
        elif(p[i] != "." and p[i] != "X" and waiting_for_coef):
            # Tant que on a pas atteint X ou . on peut continuer
            # A construire le coefficient
            coef = coef + p[i]
        elif(p[i] != "." and p[i] != "X" and has_power):
            if(power == "+1"):
                # Cela signifie qu'on est respté dans la boucle
                # La puissance peut donc être lu correctement
                # On réinitialise la valeur
                power = ""
            # Tant qu'on recherche toujours une puissance, on ajoute les chiffres qui compose la puissance 
            power = power + p[i]
        elif(p[i] == "X"):
            # On a trouvé un X, mais on ne sait pas si la boucle va se terminer
            # Si elle se termine la puissance vaudra forcément 1
            # Le plus permet de le différencier de la construction des autres puissance
            power = "+1"
            waiting_for_coef = False
        elif(p[i] == "^"):
            # Signe de puissace identifié
            has_power = True

    
    if(power == ""):
        # Sorti de la boucle, si la puissance n'est pas écrite
        # Alors elle vaut forcément 0
        power = "0"
    j: int
    for j in range(prev_power-int(power)-1):
        # On ajoute autant de 0 que de puissance qui sépare la puissance précédente à celle en sortie de boucle
        pres.append(0)
    if(coef != "" and coef != "0"):
        # On ajoute le coefficient s'il existe
        pres.append(int(coef))
    if(power != "0"):
        k: int
        for k in range(int(power)):
            # Au cas où on ne se soit pas arrêté précisément sur
            # La puissance nulle, on ajoute le nombre de 0 nécéssaire
            pres.append(0)
    return pres[::-1]

assert pdc(cdp(ex1)) == normalise(ex1)
assert pdc(cdp(ex2)) == normalise(ex2)
assert pdc(cdp(ex3)) == normalise(ex3)
assert pdc(cdp(ex4)) == normalise(ex4)
assert pdc("-X^2 + 3.X") == [0, 3, -1]
assert pdc("X^4 - 3.X") == [0, -3, 0, 0, 1]
assert pdc("0.X^2 + 3.X") == [0, 3]

def poly_file(nom: str, p2: Polyn, operation: int) -> None:
    """Préconditions: Le fichier existe et contient un polynôme covenablement formaté et operation == 0 or operation == 1 or operation == 2
    Ecrit sur le fichier donné, la valeur de l'opération entre le polynôme dans le fichier et celle donnée en fonction
    operation 0 -> addition
    operation 1 -> soustraction
    operation 2 -> multiplication"""
    with open(nom+".txt", "w") as file:
        p1: Polyn = pdc(file.readlines()[0])
        if(operation == 0):
            file.write(" + " + cdp(p2) + " = " + cdp(somme(p1, p2)))
        elif(operation == 1):
            file.write(" - " + cdp(p2) + " = " + cdp(somme(p1, p2*(-1))))
        else:
            file.write(" * (" + cdp(p2) + ") = " + cdp(produit(p1, p2)))


            
        
