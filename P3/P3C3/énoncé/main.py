# from main import main

#? écrire dans des fichiers externes
# créer un nouveau fichier .txt appelé « bonjour.txt » et y écrire « Hello, world! »
fichier = open("hello.txt", "w")
fichier.write("Hello, world!")
fichier.close()
#* Lecture et parsing du fichier hello.txt
with open("hello.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)

#* Lecture et parsing du fichier input.csv
with open("input.csv", "r") as file:
    for ligne in file:
        # faire quelque chose avec une ligne
        print(ligne)


import csv

with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)

# DictReader() Cette méthode sait que la première ligne est un en-tête, et sauvegarde les autres lignes en tant que dictionnaires. Chaque clé est un nom de colonne, et la valeur est la valeur de la colonne.
with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])

#? écrire dans des fichiers externes
# Créer une liste pour les en-têtes
en_tete = ["titre", "description"]

# Exemple de listes de titres et descriptions
titres = ["Titre 1", "Titre 2", "Titre 3"]
descriptions = ["Description 1", "Description 2", "Description 3"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)
    # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
    for titre, description in zip(titres, descriptions):
        # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
        ligne = [titre, description]
        writer.writerow(ligne)


# Ne touchez pas le code ci-dessous
    #! if __name__ == "__main__":
      #!  main()
