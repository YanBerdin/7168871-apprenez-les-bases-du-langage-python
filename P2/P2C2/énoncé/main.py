# Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : "1,2,3,4").
nombres = input("Entrez une liste de nombre séparés par des virgules : ")
# Utilisez la méthode split() pour diviser cette chaîne de caractères en une variable de type liste 'liste'
liste = nombres.split(",")

# Afficher la liste des nombres
print("Liste des nombres:", liste)
# A ce stade, 'liste' est une liste de chaînes de caractères (str).

# Transformez 'liste' en une liste d'entiers 'liste_entiers', en utilisant la fonction  int. Vous devrez convertir chaque élément un par un ! Utilisez une boucle.
liste_entiers = []
for number_in_liste in liste:
    # Nettoyage des espaces
    number_in_liste = number_in_liste.strip()
    # Vérification si c'est un nombre (positif ou négatif)
    if number_in_liste.startswith('-'):
        # Pour les nombres négatifs, vérifie si le reste est numérique
        if not number_in_liste[1:].isnumeric():
            print(f"'{number_in_liste}' n'est pas un nombre valide.")
            raise SystemExit("Fin du programme")
    elif not number_in_liste.isnumeric():
        print(f"'{number_in_liste}' n'est pas un nombre valide.")
        raise SystemExit("Fin du programme")
    # Convertissez l'élément en entier et ajoutez-le à la liste 'liste_entiers'
    liste_entiers.append(int(number_in_liste))
    
somme = 0
# Utilisez une boucle pour calculer la somme de tous les éléments de 'liste_entiers'
for number_in_liste_entiers in liste_entiers:
    somme += number_in_liste_entiers
# Affichez la somme
print(f"La somme de la liste {liste_entiers} est : {somme}")
# Utilisez la fonction len() la moyenne de tous les nombres de 'liste_entiers'
moyenne = somme / len(liste_entiers)
# Affichez la moyenne
print(f"La moyenne de la liste {liste_entiers} est : {moyenne}")
# Utilisez la fonction max() pour trouver le plus grand nombre de 'liste_entiers'
plus_grand = max(liste_entiers)
# Affichez le plus grand nombre
print(f"Le plus grand nombre de la liste {liste_entiers} est : {plus_grand}")

#* Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.
# Utilisez une boucle pour compter le nombre d'éléments supérieurs à la moyenne
nombre_au_dessus_moyenne = 0

for number_in_liste_entiers in liste_entiers:
    if number_in_liste_entiers > moyenne:
        nombre_au_dessus_moyenne += 1
# Affichez le nombre d'éléments supérieurs à la moyenne
print(f"Il y a {nombre_au_dessus_moyenne} nombres supérieurs à la moyenne de {moyenne} dans la liste {liste_entiers}.")

# Utilisez une boucle pour afficher chaque élément de 'liste_entiers' avec son index
for index, number_in_liste_entiers in enumerate(liste_entiers):
    print(f"L'élément à l'index {index} est : {number_in_liste_entiers}")

