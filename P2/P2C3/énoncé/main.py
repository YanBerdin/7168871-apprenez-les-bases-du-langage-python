# Créez une fonction appelée  salaire_mensuel(salaire_annuel)  qui prend en paramètre un salaire annuel et retourne le salaire mensuel correspondant en divisant le salaire annuel par 12.
def salaire_mensuel(salaire_annuel):
    """
    Calcule le salaire mensuel à partir du salaire annuel.
    
    :return: Le salaire mensuel.
    """
    return salaire_annuel / 12

# Créez une fonction appelée  salaire_hebdomadaire(salaire_mensuel)  qui prend en paramètre un salaire mensuel et retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4.
def salaire_hebdomadaire(salaire_mensuel):
    """
    Calcule le salaire hebdomadaire à partir du salaire mensuel.
    
    :return: Le salaire hebdomadaire.
    """
    return salaire_mensuel / 4

# Créez une fonction appelée  salaire_horaire(salaire_hebdomadaire)  qui prend en paramètre un salaire hebdomadaire et retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par 35.
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    """
    Calcule le salaire horaire à partir du salaire hebdomadaire.
    
    :param salaire_hebdomadaire: Le salaire hebdomadaire
    :param heures_travaillees: Nombre d'heures travaillées par semaine
    :return: Le salaire horaire arrondi à 2 décimales
    """
    return round(salaire_hebdomadaire / heures_travaillees, 2)

# Demandez à l'utilisateur de saisir son salaire annuel.
try:
    salaire_input = input("Entrez votre salaire annuel : ").strip()
    salaire_annuel = float(salaire_input)
    if salaire_annuel <= 0:
        raise ValueError("Le salaire doit être positif")

except ValueError:
    print("Veuillez entrer un salaire valide (nombre positif).")
    raise SystemExit("Fin du programme")

# Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine
try:
    heures_input = input("Entrez le nombre d'heures travaillées par semaine : ").strip()
    nombre_heures = float(heures_input)
    if nombre_heures <= 0:
        raise ValueError("Le nombre d'heures doit être positif")

except ValueError:
    print("Veuillez entrer un nombre d'heures valide (nombre positif).")
    raise SystemExit("Fin du programme")

# Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant
montant_mensuel = salaire_mensuel(salaire_annuel)
montant_hebdomadaire = salaire_hebdomadaire(montant_mensuel)
montant_horaire = salaire_horaire(montant_hebdomadaire, nombre_heures)

# Affichez le résultat sous la forme : "Votre salaire horaire est de XX euros".
print(f"Votre salaire horaire est de {montant_horaire} euros.")