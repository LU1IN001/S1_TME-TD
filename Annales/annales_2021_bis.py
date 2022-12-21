from typing import *
Dep = Dict[str, Set[str]]

LicenseInfo: Dep = {"BDD": {"Alice", "Bob", "Carole"}, 
                    "Lambda": {"Alice", "Bob", "Carole", "David", "Elise"}, 
                    "POO": {"Bob", "Elise"},
                    "IA": set(),
                    "Compil": {"Alice", "Bob", "David"}}

LicenseBio: Dep = {"Microbio": {"Fadia", "David"}, 
                    "Genetique": {"Fadia", "David"}, 
                    "Animale": {"Fadia"}}

LicenseMath: Dep = {"Topologie": {"Elise", "Gwenael"}, 
                    "AlgLin": {"Elise", "Gwenael"}}

Faculte2Science: List[Dep] = [LicenseBio, LicenseInfo, LicenseMath]

def effectifs_UE(d: Dep, ue: str) -> int:
    if ue in d:
        return len(d[ue])
    else:
        return 0

def etudiants(d: Dep) -> Set[str]:
    res: Set[str] = set()
    v: Set[str]
    for _, v in d.items():
        res = res | v
    return res

def inscriptions_etu(d: Dep, etu:str) -> Set[str]:
    return {k for k,v in d.items() if etu in v}

def inscriptions_tous(d: Dep) -> Dict[str, Set[str]]:
    return {etu: inscriptions_etu(d, etu) for etu in etudiants(d)}

def doubles_licenses(dl: List[Dep]) -> Set[str]:
    res: Set[str] = set()
    seen: Set[str] = set()
    d: Dep
    for d in dl:
        e: str
        for e in etudiants(d):
            if e in seen:
                res.add(e)
            seen.add(e)
    return res