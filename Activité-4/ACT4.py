# Wilhem Blondel

import random
import math

def est_majuscule(ch: str) -> bool:
    """Préconditions: len(ch) == 1
    Indique si le caractère est en majuscule ou non"""
    return 65 <= ord(ch) and ord(ch) <= 90

def est_minuscule(ch: str) -> bool:
    """Préconditions: len(ch) == 1
    Indique si le caractère est en minuscule ou non"""
    return 97 <= ord(ch) and ord(ch) <= 122


assert est_majuscule ("C")
assert not est_minuscule ("C")
assert est_minuscule ("c")
assert not est_majuscule ("c")
assert not est_minuscule (" ")
assert not est_majuscule (" ")

def caractere_decale(ch: str, n: int) -> str:
    """Préconditions: len(ch) == 1
    Retourne la lettre décalée d'un nombre choisi de place dans l'alphabet
    Si c'est impossible, on retourne seulement ch"""
    if(est_majuscule(ch) or est_minuscule(ch)):
        new_code: int = ord(ch) + n
        if(est_majuscule(ch) and est_majuscule(chr(new_code)) or est_minuscule(ch) and est_minuscule(chr(new_code))):
            return chr(new_code)
        else:
            if(n >= 0):
                return chr(new_code-26)
            else:
                return chr(new_code+26)         
    else:
        return ch

assert caractere_decale ("a", 0) == "a"
assert caractere_decale ("a", 3) == "d"
assert caractere_decale ("A", 3) == "D"
assert caractere_decale ("V", 8) == "D"
assert caractere_decale (" ", 3) == " "

def ligne_chiffre_cesar(line: str, n: int) -> str:
    """Retourne la ligne décalée de tant de lettre dans l'alphabet"""
    res: str = ""
    ch: str
    for ch in line:
        res = res + caractere_decale(ch, n)
    return res

assert ligne_chiffre_cesar (" Bonjour LU1IN011 ", 3) == " Erqmrxu OX1LQ011 "
assert ligne_chiffre_cesar (" Bonjour LU1IN011 ", 0) == " Bonjour LU1IN011 "

def ligne_dechiffre_cesar(line: str, n: int) -> str:
    """Déchiffre le code césar avec la clé indiquée"""
    res: str = ""
    ch: str
    for ch in line:
        res = res + caractere_decale(ch, -n)
    return res
    
beaute1 : str = "Je suis belle , o mortels ! comme un reve de pierre ,"
assert ligne_dechiffre_cesar (ligne_chiffre_cesar(beaute1, 12), 12) == beaute1

def chiffre_fichier_cesar(nom : str, n: int) -> None :
    """ Precondition : <nom>.txt est un fichier existant
    chiffre le contenu du fichier <nom>.txt avec un code césar de clé n dans <nom>-chiffre.txt """
    with open(nom + ".txt", "r") as source :
        with open(nom + "-chiffre.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_chiffre_cesar(ligne, n))

chiffre_fichier_cesar("C:/Users/wilhe/Desktop/Sorbonne Workspace/PPTI-Retrieved/Activité-4/albatros", 3)

def dechiffre_fichier_cesar(nom : str, n: int) -> None :
    """ Precondition : <nom>.txt est un fichier existant
    déchiffre le contenu du fichier <nom>.txt avec un code césar de clé n dans <nom>-dechiffre.txt """
    with open(nom + ".txt", "r") as source :
        with open(nom + "-dechiffre.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_dechiffre_cesar(ligne, n))


# Suggestion 3

def pick_random_number(n: int) -> int:
    """Préconditions n >= 0,
    Choisi un nombre aléatoire dzans [0, n]
    """
    random_n: float = random.random()
    i: int
    for i in range(1, n):
        if(random_n <= i/n):
            return i
    return n

# TODO random.seed test
    

def attaque_cesar(nom: str) -> None:
    """ Precondition : <nom>.txt est un fichier existant
    teste toutes les combinaisons pour déchiffrer le contenu du fichier donné et met les résultats dans <nom>-attaque.txt """
    with open(nom + ".txt", "r") as source :
        with open(nom + "-attaque.txt", "w") as destination :
            lines_of_doc: List[str] = source.readlines()
            random_start: int = pick_random_number(len(lines_of_doc))
            destination.write("Lignes choisies : "+ str(random_start) + "-" + str(random_start+5)+"\n")
            destination.write("================================\n")
            tried_key: int
            for tried_key in range(0, 27):
                destination.write("Decalage de " + str(tried_key) + "\n")
                ligne : str
                for ligne in lines_of_doc[random_start:random_start+5] :
                    destination.write(ligne_dechiffre_cesar(ligne, tried_key))
                destination.write("================================\n")


# Suggestion 4

def premier_suivant(a: int, b: int) -> int:
    """Précondtions: a >= 0 and b >= 2
    Retourne la valeur du nombre premier par rapport à b le plus proche de a ou a lui même"""
    a_copy: int = a
    if a_copy <= 1:
        a_copy = 2
    i: int = 1
    while i <= b:
        i = i + 1
        if(b%i == 0 and a_copy%i == 0):
            a_copy = a_copy + 1
            i = 1
    return a_copy

assert premier_suivant(12, 26) == 15
assert premier_suivant(15, 26) == 15
assert premier_suivant(0, 26) == 3
assert premier_suivant(2, 26) == 3


def ligne_chiffre_affine(line: str, a: int, b: int) -> str:
    """Retourne la ligne décalée de a*p + b % 26 dans l'alphabet"""
    res: str = ""
    a_transform: int = premier_suivant(a, 26)
    ch: str
    for ch in line:
        if(est_majuscule(ch)):
            res = res + chr(((a_transform*(ord(ch)-65)+b)%26)+65)
        elif(est_minuscule(ch)):
            res = res + chr(((a_transform*(ord(ch)-97)+b)%26)+97)
        else:
            res = res + ch
    return res

assert ligne_chiffre_affine("Bonjour LU1IN011!", 3, 7) == "Kxuixpg OP1FU011!"
assert ligne_chiffre_affine("Bonjour LU1IN011!", 2, 7) == "Kxuixpg OP1FU011!"
assert ligne_chiffre_affine("Bonjour LU1IN011!", 14, 47) == "Kxiaxjq EJ1LI011!"

def modulo_inverse(a: int, modulo: int) -> int:
    """Retourne le modulo inverse de a congru modulo en utilisant l'algorithme d'euclide étendu"""
    # On doit coriger la valeur de a pour que le modulo puisse être inversible
    # En effet, un modulo est inversible s.si pour a congru modulo on a et modulo premiers entre eux
    # Cela ne pose pas de problème, puisque a a été modifié de la même manière lors du chiffrement
    # Néanmoins, pour une utilisation universelle, en dehors de notre programme, il faut mieux renvoyer None ou une erreur
    a_transform: int = premier_suivant(a, modulo)
    r: int = a_transform
    r_prime: int = modulo
    u: int = 1
    v: int = 0
    u_prime: int = 0
    v_prime: int = 0
    q: int = 0
    rs: int = 0
    us: int = 0
    vs: int = 0

    while r_prime != 0:
        q = r//r_prime
        rs = r
        us = u
        vs = v
        r = r_prime
        u = u_prime
        v = v_prime
        r_prime = rs - q*r_prime
        u_prime = us -q*u_prime
        v_prime = vs - q*v_prime

    if u < 0:
        return modulo + u
    else:
        return u

assert modulo_inverse(14, 26) == 7
assert modulo_inverse(15, 26) == 7
assert modulo_inverse(17, 26) == 23

def ligne_dechiffre_affine(line: str, a: int, b: int) -> str:
    """Déchiffre le code césar avec la clé affine indiquée"""
    res: str = ""
    ch: str
    for ch in line:
        if(est_majuscule(ch)):
            res = res + chr((((ord(ch) - 65 - b) * modulo_inverse(a, 26))%26) + 65)
        elif(est_minuscule(ch)):
            res = res  + chr((((ord(ch) - 97 - b) * modulo_inverse(a, 26))%26) + 97)
        else:
            res = res + ch
    return res


assert ligne_dechiffre_affine("Kxuixpg OP1FU011!", 3, 7) == "Bonjour LU1IN011!"
assert ligne_dechiffre_affine("Kxuixpg OP1FU011!", 2, 7) == "Bonjour LU1IN011!"
assert ligne_dechiffre_affine("Kxiaxjq EJ1LI011!", 14, 47) == "Bonjour LU1IN011!"

beaute1_c : str = ligne_chiffre_affine(beaute1 , 28, 2016)
assert ligne_dechiffre_affine(beaute1_c , 28, 2016) == beaute1


def chiffre_fichier_affine(nom : str, a: int, b: int) -> None :
    """ Precondition : <nom>.txt est un fichier existant
    chiffre le contenu du fichier <nom>.txt dans <nom>-affine.txt avec un code césar affine"""
    with open(nom + ".txt", "r") as source :
        with open(nom + "-affine.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_chiffre_affine(ligne, a, b))


def dechiffre_fichier_affine(nom : str, a: int, b: int) -> None :
    """ Precondition : <nom>.txt est un fichier existant
    dechiffre le contenu du fichier <nom>.txt dans <nom>-dechiffre-affine.txt avec un code césar affine"""
    with open(nom + ".txt", "r") as source :
        with open(nom + "-dechiffre-affine.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_dechiffre_affine(ligne, a, b))


# Suggestion 5

def ligne_chiffre_vigenere(ligne: str, key: str) -> str:
    """Précondition key contient des lettres de l'alphabet latin
    Retourne la ligne donnée chiffrée par vigenere par la clé key"""
    index: int = 0
    res: str = ""
    ch: str
    letter_used: str
    for ch in ligne:
        letter_used = key[index%len(key)] 
        if(est_majuscule(letter_used)):
            res = res + caractere_decale(ch, ord(letter_used) - 65)
        elif(est_minuscule(letter_used)):
            res = res + caractere_decale(ch, ord(letter_used) - 97)
        else:
            res = res + ch
        index = index + 1
    return res

def ligne_dechiffre_vigenere(ligne: str, key: str) -> str:
    """Précondition key contient des lettres de l'alphabet latin
    Retourne la ligne donnée déchiffrée par vigenere  par la clé key"""
    index: int = 0
    res: str = ""
    ch: str
    letter_used: str
    for ch in ligne:
        letter_used = key[index%len(key)] 
        if(est_majuscule(letter_used)):
            res = res + caractere_decale(ch, -ord(letter_used) + 65)
        elif(est_minuscule(letter_used)):
            res = res + caractere_decale(ch, -ord(letter_used) + 97)
        else:
            res = res + ch
        index = index + 1
    return res

def chiffre_fichier_vigenere(nom : str, key: str) -> None :
    """ Precondition : <nom>.txt est un fichier existant, key contient des lettres de l'alphabet latin
    chiffre le contenu du fichier <nom>.txt dans <nom>-vigenre.txt avec un chiffre vigenere"""
    with open(nom + ".txt", "r") as source :
        with open(nom + "-vigenere.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_chiffre_vigenere(ligne, key))


def dechiffre_fichier_vigenere(nom : str, key: str) -> None :
    """ Precondition : <nom>.txt est un fichier existant, key contient des lettres de l'alphabet latin
    dechiffre le contenu du fichier <nom>.txt dans <nom>-dechiffre-vigenere.txt avec un chiffre vigenere"""
    with open(nom + ".txt", "r") as source :
        with open(nom + "-dechiffre-vigenere.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_dechiffre_vigenere(ligne, key))
        
        
assert ligne_chiffre_vigenere("Bonjour","cle") == "Dzrlzyt"
assert ligne_chiffre_vigenere("Bonjour LU1IN011!", "AAA") == "Bonjour LU1IN011!"
assert ligne_chiffre_vigenere("Bonjour LU1IN011!", "Maths") == "Nogqggr SM1IG011!"
assert ligne_chiffre_vigenere("Bonjour LU1IN011!", "c") == ligne_chiffre_cesar("Bonjour LU1IN011!", 2)
assert ligne_dechiffre_vigenere(ligne_chiffre_vigenere(beaute1 , "beaute"), "beaute") == beaute1

# Suggestion 6 (Pas réussie)

def divisible_suivant(a: int, b: int) -> int:
    """Préconditions: b > 0
    Renvoie le nombre au plus proche de  ou a lui même divisible par b
    """
    a_copy: int = a
    while(a_copy%b != 0):
        a_copy = a_copy + 1
    return a_copy

assert divisible_suivant(10, 3) == 12

def ligne_chiffre_scytale(ligne: str, perimetre: int) -> str:
    """Précondition perimetre > 0
    Retourne la ligne donnée chiffrée par scytale par la clé perimetre donnée"""
    line_size: int = divisible_suivant(len(ligne), perimetre) // perimetre
    res: str = ""
    k: int
    i: int
    for k in range(line_size):
        for i in range(perimetre):
            if(len(ligne) > line_size*i+k):
                res =  res + ligne[line_size*i+k]
    return res

def ligne_dechiffre_scytale(ligne: str, perimetre: int) -> str:
    """Précondition perimetre > 0
    Retourne la ligne donnée déchiffrée par scytale par la clé perimetre donnée"""
    line_size: int = divisible_suivant(len(ligne), perimetre) // perimetre
    to_deduct: int = perimetre*line_size - len(ligne)
    to_deduct_const: int  = to_deduct
    res: str = ""
    i: int
    k: int
    for i in range(perimetre):
        for k in range(line_size+1):
            if k == line_size - to_deduct_const + 1 and to_deduct != 0:
                   res = res + ligne[i + k*perimetre - 1 ]
                   to_deduct = to_deduct - 1
            elif i > to_deduct - 1 and len(ligne) > i + k*perimetre + to_deduct_const:
                res = res + ligne[i + k*perimetre]
            elif len(ligne) > i + k*perimetre + to_deduct_const:
                res = res + ligne[i + k*perimetre]
    return res
            

assert ligne_chiffre_scytale("0123456789", 1) == "0123456789"
assert ligne_chiffre_scytale("0123456789", 2) == "0516273849"
assert ligne_chiffre_scytale("0123456789", 3) == "0481592637"
assert ligne_chiffre_scytale("0123456789", 5) == "0246813579"
assert ligne_dechiffre_scytale("0246813579", 5) == "0123456789"
assert ligne_dechiffre_scytale("0481592637", 3) == "0123456789"
beaute1_s: str = ligne_chiffre_scytale(beaute1 , 4)
assert ligne_dechiffre_scytale(beaute1_s, 4) == 'Je suis belle, o mortels !comme un revede pierre ,e'
