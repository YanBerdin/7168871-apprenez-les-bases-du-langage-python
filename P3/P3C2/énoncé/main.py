
from bs4 import BeautifulSoup
# import requests

# url = "https://www.gov.uk/search/news-and-communications"
# page = requests.get(url)

# Voir le code html source
# print(page.content)

#* Lecture et parsing du fichier HTML
with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')

# print(soup.prettify())#todo: supprimer

# Extraction du titre de la page
title = soup.title.string
print("\nTitre de la page:", title)

# Récupérer l'élément avec la balise <h1> complète
#`<h1 id="titre">Bienvenue sur notre site web</h1>` (un élément HTML)
h1_html_element = soup.find("h1")
print("\nbalise html h1:", h1_html_element) #todo: supprimer

# Récupérer la String contenue dans la balise h1
h1_text = soup.find("h1").string
print("\nTitre principal (h1):", h1_text)

# Dictionnaire pour stocker les produits à récupérer
all_products_dict = dict()

# Préparer liste descriptions
descriptions_list = []

print("\nListe des produits:")

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all("li", class_="product")
print("\nproducts:", products) #todo: supprimer

for product in products:
    # Récupérer l'élément <h2>
    name = product.find("h2").string
    print(f"\n- name : {name}") #todo: supprimer

    # Récupérer l'élément <p> de classe "price" => Prix: 10€
    price_str = product.find("p", class_="price").string
    print(f" price_str : {price_str}") #todo: supprimer

    # Séparer la chaine avec " " en liste[] de string => ['Prix:', '10€']
    price_list = price_str.split(" ")
    print(f" price_list : {price_list}") #todo: supprimer

    # On push le prix en € (= 2ème mot) dans all_products_dict à l'index name récupéré
    all_products_dict[name] = {"prix": price_list[1]}
    print(f" all_products_dict {all_products_dict}") #todo: supprimer

    # Récupèrer la description = Dernier élément de la liste des <p>
    description = product.find_all("p")[-1].string
    
    # Push la description dans all_products_dict au même index name récupéré
    all_products_dict[name]["description"] = description
    
    print(f"\n- {name}")
    print(f"  {price_str}")
    print(f"  {description}")
    print("\nall_products_dict:", all_products_dict)

# Ajout des prix en $
for name in all_products_dict.keys():
    price_str = all_products_dict[name]["prix"]
    # Supprimer le symbole € + convertir en float
    price = float(price_str.strip("€"))
    # Convertir en $ (1€ = 1.2$)
    dollar_price = price * 1.2
    # Pusher le prix en $ dans le dictionnaire
    all_products_dict[name]["prix_dollar"] = f"{dollar_price:.2f}$"
    print("\nall_products_dict + prix_dollar :", all_products_dict) #todo: supprimer

# Affichage final avec les prix en euros et en $
print("\nProduits avec prix en euros et $:")
for name, details in all_products_dict.items():
    print(f"\n- {name}")
    print(f"  Prix: {details['prix']}")
    print(f"  Prix en $: {details['prix_dollar']}")
    print(f"  Description: {details['description']}")
