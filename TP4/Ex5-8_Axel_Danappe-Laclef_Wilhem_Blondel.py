def decompression(chaine: str) -> str:
    """Décompresse la chaîne de caractère donnée"""
    ch: str
    duplicate: int = 1
    res: str = ""
    did: bool = False
    for ch in chaine:
        if(duplicate > 1):
            res = res + ch * duplicate
            did = True
        if(ch >= '0' and ch <= '9'):
            duplicate = int(ch)
        elif(not did and duplicate == 1):
            res = res + ch
        else:
            duplicate = 1
            did = False
            
    return res

assert decompression('ab3cd') == "abcccd"
assert decompression('ab3c2d4efgh') == 'abcccddeeeefgh'
assert decompression('abcdefg') == 'abcdefg'
assert decompression('abcd2c') == 'abcdcc'




def compression(chaine: str) -> str:
    """Compresse la chaîne de caractère renseignée"""
    count: int = 1
    res: str = ""
    i: int
    for i in range(len(chaine)):
        if(i == len(chaine) - 1):
            if(count > 1):
                return res + str(count) + chaine[i]
            else:
                return res + chaine[i]
        if(chaine[i] == chaine[i+1]):
            count = count + 1
        elif(count > 1):
            res = res + str(count) + chaine[i]
            count = 1
        else:
            res = res + chaine[i]


assert compression(decompression('ab3cd')) == 'ab3cd'
assert compression(decompression('ab3c2d4efgh')) == 'ab3c2d4efgh'
assert compression(decompression('abcdefg')) == 'abcdefg'
assert compression(decompression('abcd2c')) == 'abcd2c'
