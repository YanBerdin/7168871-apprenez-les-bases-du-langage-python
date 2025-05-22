# from operations import addition 
import operations 

def main():
    # Demander à l'utilisateur de saisir deux nombres
    try:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        return

    # Calculer la somme
    # resultat = addition(a, b)
    resultat = operations.addition(a, b)

    # Afficher le résultat
    print(f"La somme de {a} et {b} est {resultat}.")
if __name__ == "__main__":
    main()

