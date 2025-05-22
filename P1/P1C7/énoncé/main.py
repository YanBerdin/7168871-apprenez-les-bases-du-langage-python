# 1. **Créez** un **dictionnaire** appelé `fruits` avec les clés `"pomme"`, `"banane"` et `"orange"`, et respectivement les valeurs `"rouge"`, `"jaune"` et `"orange"`.
fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}
# 2. **Ajoutez** la clé `"kiwi"` avec la valeur `"vert"` au dictionnaire `fruits`.
fruits["kiwi"] = "vert"
# 3. **Accédez** à la valeur correspondant à la clé `"banane"` et stockez-la dans une variable appelée `couleur_banane`.
couleur_banane = fruits["banane"]
# 4. **Modifiez** la valeur associée à la clé `"pomme"` pour `"vert"`. 
fruits["pomme"] = "vert"
# 5. **Supprimez** la clé `"banane"` du dictionnaire `fruits`.
del fruits["banane"]
# 6. **Affichez** les clés restantes dans le dictionnaire.
print(fruits.keys())
# 7. **Affichez** les valeurs restantes dans le dictionnaire.
print(fruits.values())
# 8. **Vérifiez** si la clé `"orange"` existe dans le dictionnaire `fruits` et affichez un message approprié.
if "orange" in fruits:
    print("La clé 'orange' existe dans le dictionnaire.")
else:
    print("La clé 'orange' n'existe pas dans le dictionnaire.")
