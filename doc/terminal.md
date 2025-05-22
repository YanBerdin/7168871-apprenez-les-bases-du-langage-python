```bash
-les-bases-du-langage-python/P2/P2C3/énoncé$ python3 main.py
Entrez votre salaire annuel : 0000
Veuillez entrer un salaire valide (nombre positif).
Fin du programme
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P2/P2C3/énoncé$ python3 main.py
Entrez votre salaire annuel : ....
Veuillez entrer un salaire valide (nombre positif).
Fin du programme
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P2/P2C3/énoncé$ python3 main.py
Entrez votre salaire annuel : .333
Entrez le nombre d'heures travaillées par semaine : 3
Votre salaire horaire est de 0.0 euros.
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P2/P2C3/énoncé$ 
 *  History restored 

yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P2/P2C3/énoncé$ cd ..
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P2/P2C3$ cd ..
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P2$ cd ..
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python$ cd P3
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ ls
P3C1  P3C2  P3C3
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ cd P3C2
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2$ pip install beautifulsoup4
Command 'pip' not found, but can be installed with:
sudo apt install python3-pip
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2$ cd énoncé/
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ pip install beautifulsoup4
Command 'pip' not found, but can be installed with:
sudo apt install python3-pip
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ python3 -m venv env
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ source env/bin/activate
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ pip install beautifulsoup4
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.13.4-py3-none-any.whl.metadata (3.8 kB)
Collecting soupsieve>1.2 (from beautifulsoup4)
  Downloading soupsieve-2.7-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4)
  Downloading typing_extensions-4.13.2-py3-none-any.whl.metadata (3.0 kB)
Downloading beautifulsoup4-4.13.4-py3-none-any.whl (187 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 187.3/187.3 kB 99.9 kB/s eta 0:00:00
Downloading soupsieve-2.7-py3-none-any.whl (36 kB)
Downloading typing_extensions-4.13.2-py3-none-any.whl (45 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.8/45.8 kB 230.0 kB/s eta 0:00:00
Installing collected packages: typing-extensions, soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.13.4 soupsieve-2.7 typing-extensions-4.13.2
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ deactivate
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ rm -rf /home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé/env
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ source /home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/env/bin/activate
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ which python
/home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/env/bin/python
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ which python
/home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/env/bin/python
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ pip uninstall beautifulsoup4
WARNING: Skipping beautifulsoup4 as it is not installed.
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ deactivate
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ cd ~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2
source env/bin/activate
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2$ which python
/home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/env/bin/python
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2$ pip install beautifulsoup4
Collecting beautifulsoup4
  Using cached beautifulsoup4-4.13.4-py3-none-any.whl.metadata (3.8 kB)
Collecting soupsieve>1.2 (from beautifulsoup4)
  Using cached soupsieve-2.7-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4)
  Using cached typing_extensions-4.13.2-py3-none-any.whl.metadata (3.0 kB)
Using cached beautifulsoup4-4.13.4-py3-none-any.whl (187 kB)
Using cached soupsieve-2.7-py3-none-any.whl (36 kB)
Using cached typing_extensions-4.13.2-py3-none-any.whl (45 kB)
Installing collected packages: typing-extensions, soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.13.4 soupsieve-2.7 typing-extensions-4.13.2
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-ap
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2$ ^C
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2$ cd /home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3
python3 -m venv env
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ source env/bin/activate
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ pip install beautifulsoup4 requests
Collecting beautifulsoup4
  Using cached beautifulsoup4-4.13.4-py3-none-any.whl.metadata (3.8 kB)
Collecting requests
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting soupsieve>1.2 (from beautifulsoup4)
  Using cached soupsieve-2.7-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4)
  Using cached typing_extensions-4.13.2-py3-none-any.whl.metadata (3.0 kB)
Collecting charset-normalizer<4,>=2 (from requests)
  Using cached charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (35 kB)
Collecting idna<4,>=2.5 (from requests)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Using cached urllib3-2.4.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests)
  Using cached certifi-2025.4.26-py3-none-any.whl.metadata (2.5 kB)
Using cached beautifulsoup4-4.13.4-py3-none-any.whl (187 kB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached certifi-2025.4.26-py3-none-any.whl (159 kB)
Using cached charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (148 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached soupsieve-2.7-py3-none-any.whl (36 kB)
Using cached typing_extensions-4.13.2-py3-none-any.whl (45 kB)
Using cached urllib3-2.4.0-py3-none-any.whl (128 kB)
Installing collected packages: urllib3, typing-extensions, soupsieve, idna, charset-normalizer, certifi, requests, beautifulsoup4
Successfully installed beautifulsoup4-4.13.4 certifi-2025.4.26 charset-normalizer-3.4.2 idna-3.10 requests-2.32.3 soupsieve-2.7 typing-extensions-4.13.2 urllib3-2.4.0
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ cd /home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ which python
/home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/env/bin/python
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ 
 *  History restored 

yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ which python
yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ cd /home/yandev/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3
source env/bin/activate
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ 
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ .\env\Scripts\activate
.envScriptsactivate: command not found
```

```bash
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ source env/bin/activate
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ pip install requests beautifulsoup4
Requirement already satisfied: requests in ./env/lib/python3.12/site-packages (2.32.3)
Requirement already satisfied: beautifulsoup4 in ./env/lib/python3.12/site-packages (4.13.4)
Requirement already satisfied: charset-normalizer<4,>=2 in ./env/lib/python3.12/site-packages (from requests) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in ./env/lib/python3.12/site-packages (from requests) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./env/lib/python3.12/site-packages (from requests) (2.4.0)
Requirement already satisfied: certifi>=2017.4.17 in ./env/lib/python3.12/site-packages (from requests) (2025.4.26)
Requirement already satisfied: soupsieve>1.2 in ./env/lib/python3.12/site-packages (from beautifulsoup4) (2.7)
Requirement already satisfied: typing-extensions>=4.0.0 in ./env/lib/python3.12/site-packages (from beautifulsoup4) (4.13.2)
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ pip list | grep -E "beautifulsoup4|requests"
beautifulsoup4     4.13.4
requests           2.32.3
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3$ cd P3C2
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2$ cd énoncé/
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ python3 main.py
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ soup.title
soup.title: command not found
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ python main.py
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ python main.py
Titre de la page: Exercice extraction HTML

Titre principal (h1): Bienvenue sur notre site web

Liste des produits:

- Produit 1
  Prix: 10€
  Description : Lorem ipsum dolor sit amet, consectetur adipiscing elit.

- Produit 2
  Prix: 20€
  Description : Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

- Produit 3
  Prix: 30€
  Description : Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
(env) yandev@LAPTOP-CE57E7VI:~/projets/python_projects/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé$ 

```
