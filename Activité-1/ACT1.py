# Wilhem Blondel
import random

def sujet(index: int) -> str:
    """
    Preconditions: index>= 1 et index <= 12
    retourne un sujet correspondant a la valeur
    """
    if(index==1): return "Kevin"
    if(index==2): return "Brandon"
    if(index==3): return "Dagobert"
    if(index==4): return "Axel"
    if(index==5): return "Annie" 
    if(index==6): return "Elsa" 
    if(index==7): return "Steven"
    if(index==8): return "Alfred"
    if(index==9): return "Charlotte" 
    if(index==10): return "Camille"
    if(index==11): return "John"
    return "Rodrigue"

assert sujet(3) == "Dagobert"
assert sujet(5) == "Annie"

def est_feminin(index_sujet: int) -> bool:
    """
    Preconditions: index_sujet>= 1 et index_sujet <= 12
    retourne un boolean indiquant si le sujet est féminin
    """
    if(index_sujet == 5 or index_sujet == 6 or index_sujet == 9 or index_sujet == 10): 
        return True
    return False

assert est_feminin(9) == True
assert est_feminin(11) == False

def adjectif(index_sujet:int, index: int) -> str:
    """
    Preconditions: index>= 1 et index <= 6 et index_sujet >=1 et index_sujet <= 24
    retourne un adjectif correspondant a la valeur
    """
    if(index==1):
        if(est_feminin(index_sujet)): return "la rigolote"
        return "le rigolo"
    if(index==2):
        if(est_feminin(index_sujet)): return "la pâlichonne"
        return "le pâlichon"
    if(index==3): 
        if(est_feminin(index_sujet)): return "la pleureuse"
        return "le pleureur"
    if(index==4): 
        if(est_feminin(index_sujet)): return "la pereuse"
        return "le peureux"
    if(index==5): 
        if(est_feminin(index_sujet)): return "la bavarde"
        return "le bavard"
    if(est_feminin(index_sujet)): return "la meilleure"
    return "le meilleur"

assert adjectif(6, 3) == "la pleureuse"
assert adjectif(3, 4) == "le peureux"

def verbe(index: int) -> str:
    """
    Preconditions: index >= 1 et index <= 12
    retourne un verbe correspondant a la valeur
    """
    if(index==1): return "mange"
    if(index==2): return "range"
    if(index==3): return "apprehende"
    if(index==4): return "cuisine"
    if(index==5): return "detruit"
    if(index==6): return "aneantit"
    if(index==7): return "perturbe"
    if(index==8): return "dort"
    if(index==9): return "va"
    if(index==10): return "traumatise"
    if(index==11): return "arrive"
    else: return "humilie"

def est_transitif(index_verbe: int) -> bool:
    """
    Preconditions: index_verbe >= 1 et index_verbe <= 12
    retourne un boolean pour savoir si le verbe est transitif
    """
    if(index_verbe == 8 or index_verbe == 9 or index_verbe == 11): return True
    return False

assert est_transitif(9) == True
assert est_transitif(3) == False

def cod(index: int) -> str:
    """
    Preconditions: index >= 1 et index <= 12
    retourne un cod correspondant a la valeur
    """
    if(index==1): return "du chocolat"
    if(index==2): return "la louche"
    if(index==3): return "le train"
    if(index==4): return "des escargots"
    if(index==5): return "son gendre"
    if(index==6): return "Roger Federer"
    if(index==7): return "les citoyens"
    if(index==8): return "le pot de fleur"
    if(index==9): return "l'aspirateur"
    if(index==10): return "le porte-monnaie"
    if(index==11): return "la montagne"
    else: return "la lune"

def lieu(index: int) -> str:
    """
    Preconditions: index >= 1 et index <= 12
    retourne un lieu correspondant a la valeur
    """
    if(index==1): return "en Australie"
    if(index==2): return "dans la foret"
    if(index==3): return "sous le soleil"
    if(index==4): return "au carnaval"
    if(index==5): return "chez ses parents"
    if(index==6): return "a Paris"
    if(index==7): return "a la plage"
    if(index==8): return "sur la Tour Eiffel"
    if(index==9): return "dans le grand canyon"
    if(index==10): return "a l'ecole"
    if(index==11): return "au poste"
    else: return "en Ecosse"

assert verbe(1) == "mange"
assert verbe(5) == "detruit"
assert cod(1) == "du chocolat"
assert cod(4) == "des escargots"
assert lieu(2) == "dans la foret"
assert lieu(6) == "a Paris"

def phrase(sujet_i: int, verbe_i: int, cod_i: int, lieu_i: int) -> str:
    """
    Préconditions params >= 1 et params <= 12 sauf adj_i >= 1 et adj_i <= 12
    retourne une phrase à partir des index indiqués
    """
    return sujet(sujet_i)+" "+verbe(verbe_i)+" "+cod(cod_i)+" "+lieu(lieu_i)+"."

assert phrase(3,1,1,2) == "Dagobert mange du chocolat dans la foret."

def phrase_adj(sujet_i: int, adj_i: int, verbe_i: int, cod_i: int, lieu_i: int) -> str:
    """
    Préconditions params >= 1 et params <= 12 sauf adj_i >= 1 et adj_i <= 6
    retourne une phrase avec un adjectif au sujet à partir des index indiqués
    """
    return sujet(sujet_i)+" "+adjectif(sujet_i, adj_i)+" "+verbe(verbe_i)+" "+cod(cod_i)+" "+lieu(lieu_i)+"."

assert phrase_adj(3,1,1,1,2) == "Dagobert le rigolo mange du chocolat dans la foret."

def phrase_sans_cod(sujet_i: int, adj_i: int, verbe_i: int, lieu_i: int) -> str:
    """
    Préconditions params >= 1 et params <= 12 sauf adj_i >= 1 et adj_i <= 6
    retourne une phrase avec un adjectif au sujet mais sans COD à partir des index indiqués
    """
    return sujet(sujet_i)+" "+adjectif(sujet_i, adj_i)+" "+verbe(verbe_i)+" "+lieu(lieu_i)+"."

assert phrase_sans_cod(3,1,9,2) == "Dagobert le rigolo va dans la foret."
    

def phrase_def_sujet_adj(sujet_str: str, adj_str: str, verbe_i: int, cod_i: int, lieu_i: int) -> str:
    """
    Préconditions params >= 1 et params <= 12
    retourne une phrase à partir des index indiqués
    """
    return sujet_str+" "+adj_str+" "+verbe(verbe_i)+" "+cod(cod_i)+" "+lieu(lieu_i)+"."

assert phrase_def_sujet_adj("Albert", "le richard", 1, 1, 2) == "Albert le richard mange du chocolat dans la foret."

def de6() -> int:
    """
    retourne une valeur int aléatoire entre 1 et 6
    """
    random_n: float = random.random()
    if(random_n <= 1/6): return 1
    if(random_n <= 2/6): return 2
    if(random_n <= 3/6): return 3
    if(random_n <= 4/6): return 4
    if(random_n <= 5/6): return 5
    else: return 6

def de12() -> int:
    """
    retourne une valeur int aléatoire entre 1 et 12
    """
    random_n: float = random.random()
    if(random_n <= 1/12): return 1
    if(random_n <= 2/12): return 2
    if(random_n <= 3/12): return 3
    if(random_n <= 4/12): return 4
    if(random_n <= 5/12): return 5
    if(random_n <= 6/12): return 6
    if(random_n <= 7/12): return 7
    if(random_n <= 8/12): return 8
    if(random_n <= 9/12): return 9
    if(random_n <= 10/12): return 10
    if(random_n <= 11/12): return 11
    else: return 12

def phrase_aleatoire() -> str:
    """
    retourne une phrase aléatoire
    """
    return phrase(de6(), de6(), de6(), de6())

def phrase_aleatoire_adj() -> str:
    """
    retourne une phrase aléatoire avec un adjectif au sujet
    """
    return phrase_adj(de12(), de6(), de12(), de12(), de12())

def phrase_aleatoire2() -> str:
    """
    retourne une phrase aléatoire avec un adjectif au sujet
    et n'affiche pas de cod si le verbe aléatoire choisit est transitif
    """
    random_verb: int = de12()
    if(est_transitif(random_verb)): return phrase_sans_cod(de12(), de6(), random_verb, de12())
    return phrase_adj(de12(), de6(), random_verb, de12(), de12())


def phrase_aleatoire_sujet_adj(sujet: str, adj: str) -> str:
    """
    retourne une phrase aléatoire avec sujet prédéfinit
    """
    return phrase_def_sujet_adj(sujet, adj, de12(), de12(), de12())

