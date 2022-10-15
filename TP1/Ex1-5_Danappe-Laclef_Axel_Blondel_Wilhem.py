def fahrenheit_vers_celsius(t: float) -> float:
    """
    Retourne la conversion en fahrenheit vers celsius
    """
    return (t-32)*(5/9)
assert fahrenheit_vers_celsius(212) == 100.0
assert fahrenheit_vers_celsius(32) == 0.0
assert fahrenheit_vers_celsius(41) == 5.0

def celsius_vers_fahrenheit (t: float) -> float:
    """
    Retourne la conversion celsius vers fahrenheit
    """
    return (9/5)*t+32

assert celsius_vers_fahrenheit(100) == 212.0
assert celsius_vers_fahrenheit(0) == 32.0
assert celsius_vers_fahrenheit(5) == 41.0
