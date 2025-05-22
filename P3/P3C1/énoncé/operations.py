# addition(a, b): qui retourne la somme de deux nombres a et b 
def addition(a, b):
    """
    Calcule la somme de deux nombres.
    
    :param a: Le premier nombre
    :param b: Le deuxième nombre
    :return: La somme de a et b
    """
    return a + b

# multiplication(a, b): qui retourne le produit de deux nombres a et b
def multiplication(a, b):
    """
    Calcule le produit de deux nombres.
    
    :param a: Le premier nombre
    :param b: Le deuxième nombre
    :return: Le produit de a et b
    """
    return a * b
# soustraction(a, b): qui retourne la différence entre deux nombres a et b
def soustraction(a, b):
    """
    Calcule la différence entre deux nombres.
    
    :param a: Le premier nombre
    :param b: Le deuxième nombre
    :return: La différence entre a et b
    """
    return a - b
# division(a, b): qui retourne le quotient de deux nombres a et b
def division(a, b):
    """
    Calcule le quotient de deux nombres.
    
    :param a: Le numérateur
    :param b: Le dénominateur
    :return: Le quotient de a et b
    """
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return a / b