
from bs4 import BeautifulSoup
# import requests

# url = "https://www.gov.uk/search/news-and-communications"
# page = requests.get(url)

# Voir le code html source
# print(page.content)

# Lecture et parsing du fichier HTML
with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')

# Extraction du titre de la page
title = soup.title.string
print("Titre de la page:", title)

# Extraction du texte de la balise h1
h1_text = soup.find("h1").string
print("\nTitre principal (h1):", h1_text)

# Extraction des produits
print("\nListe des produits:")
products = soup.find_all("li", class_="product")
for product in products:
    name = product.find("h2").string
    price = product.find("p", class_="price").string
    description = product.find_all("p")[-1].string  # Dernier paragraphe = description
    
    print(f"\n- {name}")
    print(f"  {price}")
    print(f"  {description}")
