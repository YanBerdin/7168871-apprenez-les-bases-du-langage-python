# Demandez à l'utilisateur de fournir deux nombres avec la fonction input. Stockez ces valeurs dans  nombre1 et  nombre2.
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")

# nombre1et  nombre2sont des chaînes de caractères (str). 

#TODO (isnumeric)[https://docs.python.org/3/library/stdtypes.html#str.isnumeric]

# Utilisez la fonction isnumeric() pour vérifier que ce sont des nombres.
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Veuillez entrer des nombres valides.")
    # Sortez du programme en générant une exception avec le mot clé raise
    raise SystemExit("Fin du programme")

# Convertissez les deux nombres en nombres entiers avec la fonction int.
nombre1 = int(nombre1)
nombre2 = int(nombre2)

# Créez une variable operation et utilisez input pour obtenir l'opération souhaitée par l'utilisateur.
operation = input("Entrez l'opération souhaitée (+, -, *, /) : ")

# Vérifiez que l'opération est valide (+, -, * ou /). Sinon, quittez le programme.
if operation not in ['+', '-', '*', '/']:
    print("Opération non valide.")
    # Sortez du programme en générant une exception avec le mot clé raise
    raise SystemExit("Fin du programme")

match operation:
    case '+':
        resultat = nombre1 + nombre2
    case '-':
        resultat = nombre1 - nombre2
    case '*':
        resultat = nombre1 * nombre2
    case '/':
        # Si le deuxième nombre est 0 => quitter le programme 
        if nombre2 == 0:
            print("Le deuxième nombre ne peut pas être 0.")
            # Sortez du programme en générant une exception avec le mot clé raise
            raise SystemExit("Fin du programme")
        
        resultat = round(nombre1 / nombre2, 2)

# Affichez le résultat de l'opération.
print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat if operation != '/' else round(resultat, 2)}")

# str.isnumeric()
# Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.


