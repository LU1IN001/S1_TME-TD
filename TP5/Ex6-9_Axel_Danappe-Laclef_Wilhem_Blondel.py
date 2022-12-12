from typing import List
def jonction(l: List[str], c: str) -> str:
    """Précondition : len(c) = 1
    Retourne la chaîne composée de la jonction des
    chaîne de L séparées deux-à-deux par le
    caractère séparateur c."""
    res: str = ""
    i: int
    for i in range(len(l)):
        if (i != len(l) - 1):
            res = res + l[i] + c
        else:
            res = res + l[i]
    return res

assert jonction(['un', 'deux', 'trois', 'quatre'], '.') == 'un.deux.trois.quatre'
assert jonction(['les', 'mots', 'de', 'cette', 'phrase'], ' ') == 'les mots de cette phrase'
assert jonction(['un'], '+') == 'un'
assert jonction([], '+') == ''

def separation(s: str, c: str) -> List[str]:
    """Précondition : len(c) = 1
    retourne la liste de chaînes composées des sous-chaînes
    de s séparées par le caractère séparateur c.
    Le séparateur c n'est pas présent dans la chaîne résultat."""
    res: List[str] = []
    i: int
    decalage: int = 0
    for i in range(len(s)):
        if i == len(s) - 1:
           res.append(s[i - decalage:]) 
        elif(s[i] == c):
            res.append(s[i - decalage: i])
            decalage = 0
        else:
            decalage = decalage + 1
    return res

assert separation('un.deux.trois.quatre', '.') == ['un', 'deux', 'trois', 'quatre']
assert separation('les mots de cette phrase', ' ') == ['les', 'mots', 'de', 'cette', 'phrase']
assert separation('les mots de cette phrase', '.') == ['les mots de cette phrase']
assert separation('', '+') == []
