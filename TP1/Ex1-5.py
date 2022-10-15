def fahrenheit_vers_celsius(t: float) -> float:
    """
    Retourne la conversion en fahrenheit vers celsius
    """
    return (t-32)*(5/9)
assert fahrenheit_vers_celsius(212) == 100.0
assert fahrenheit_vers_celsius(32) == 0.0
assert fahrenheit_vers_celsius(41) == 5.0

def cesius_vers_fahrenheit (t: float) -> float:
    """
    Retroune la conversion celsius vers fahrenheit
    """
    return (t+32)*(9/5)

assert fahrenheit_vers_celsius(212) == 100.0
assert fahrenheit_vers_celsius(32) == 0.0
assert fahrenheit_vers_celsius(41) == 5.0
