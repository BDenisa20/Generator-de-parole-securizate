Documentatie Tehnica - Proiect Sincretic MAP 2025-2026
# Generator-de-parole-securizate

## Motivarea și scopul proiectului:
  # Motivarea
 Acest proiect a fost realizat in cadrul disciplinei Metode Avansate de Programare, la Universitatea Politehnica Timișoara, specializarea Informatica
 
  # Scopul 
 Scopul principal al proiectului este dezvoltarea unui instrument CLI(Command Line Interface) care permite:
  -generarea de parole puternice și memorabile,
  -analiza puterii unei parole existente pe baza entropiei,
  -identificarea parolelor slabe și oferirea de sugestii de îmbunătățire,
  -salvarea unui istoric securizat al parolelor analizate.

## Detalii de implementare:
 Proiectul a fost implementat folosind limbajul Python, utilizând exclusiv biblioteci standard, fără dependențe externe.

## Descriere fișiere: 
# main.py 
Gestionează argumentele din linia de comandă și coordonează apelarea funcțiilor de generare, analiză și stocarea a parolelor.

# generator.py
Generează parole complexe, memorabile. Utilizatorul iși poate personaliza lungimea și setul de caractere.

# analyzer.py
Analizează parolele generate sau introduse de utilizator, calculând entropia parolei, nivelul de securitate și scorul general al parolei.

# storage.py 
Gestionează salvarea istoricului analizelor într-un fisier JSON. Parolele sunt stocate sub formă de hash pentru siguranță.

## Explicația funcților: 
   
   # Generarea parolelor (generator.py)
-generate_password()
Generează parole aleatoare folosind caractere selectate de utilizator.
Utilizează modulul secrets pentru generare sigură criptografic.
Permite configurarea:lungimii parolei,literelor mari,cifrelor,caracterelor speciale.

-generate_memorable_password()
Creează parole ușor de reținut, formate din cuvinte separate prin delimitatori.
Oferă un compromis între securitate și memorabilitate.

   # Analizarea securității parolelor(analyzer.py)
-analyzer_password()
Evaluează nivelul de securitate al unei parole și returnează rezultatele parolei
Determină lungimea parolei, identifica tipurile de caractere utilizate, calculează entropia și clasifică parola într-o categorie de securitate 

-calculate_entropy()
Calculeaza entropia parolei, folosind lungimea parolei și numărul de caractere distincte posibile.
Entropia oferă o evaluare obiectivă a rezistenței parolei la atacuri de tip brute-force.

-get_strength()
Transforma valoarea entropiei într-o clasificare ușor de înteles.

   # Stocarea informaților (storage.py)
-hash_password()
Transformă parola într-un hash criptografic folosind algoritmul SHA-256.
Parola nu este stocată niciodată în clar, reducând riscul de compromitere a datelor.

-save_analysis()
Salvează rezultatul analizei într-un fișier JSON.Creează un obiect care conține:hash-ul parolei,entropia, nivelul de securitate, scorul,data și ora analizei.

   # Programul principal(main.py)
Coordonează execuția întregii aplicații.Definește argumentele din linia de comandă, preia opțiunile utilizatorului, apeleaza funcțiile de generare, analiză și stocare, iar la final afișaza rezultatul in terminal. 

## Tehnologii folosite:
-Limbaj de programare: Python 3.11
-Gestionarea mediului: Docker (pentru containerizare și rulare reproductibilă)
-Control versiuni: Git
-Editor cod: Visual Studio Code 
-Biblioteci: doar standard Python (fără pachete externe)

## Mediul de dezvoltare:
-Sistem de operare: Windows 10
-Editor/IDE: Visual Studio Code
-Python 3.11 instalat local
-Docker (pentru rulare container, opțional)
-Control versiuni: Git

## Bibliografie
-Curs Metode Avansate de Programare, Universitatea Politehnica Timișoara, 2025-2026
-Documentația oficială Python https://docs.python.org/3/
-Resurse despre criptografie și entropie parole
-Asistență ChatGPT pentru optimizarea codului

## Pașii de rulare a proiectului:
# cu Docker:
se copiaza comanda: docker pull denisaaaa/generator-parole:latest

se rulează folosind comanda: docker run --rm denisaaaa/generator-parole --length 16 --digits --special

# fara Docker (rulare locală):
python main.py --length 16 --upper --digits --special

python main.py --check parola123

python main.py --memorable --words 3

python main.py --batch 5

python main.py --history view

## Exemplu de output:
# fara Docker (rulare locala)
python main.py --length 16 --upper --digits --special
Parola generata: k0T^v>O?4)Uwcl!e
Putere: FOARTE PUTERNICA
Entropie: 104.87
Salvata in istoric

python main.py --check parola12
Analiza parolei "parola12":
Putere: MEDIE(50/100)
Probleme:
- Prea scurta
- Lipsesc litere mari
- Lipsesc caractere speciale
Sugestii:
- Creste lungimea parolei
- Adauga litere mari
- Adauga caractere speciale

python main.py --memorable --words 3
Parola memorabila generata: munte-caine-stele
Putere: FOARTE PUTERNICA
Entropie: 99.59
Salvata in istoric
# cu Docker 
docker run --rm denisaaaa/generator-parole --length 16 --digits --special
docker pull denisaaaa/generator-parole:latest
Parola generata: !7l{1%z3wt*:$,v{
Putere: FOARTE PUTERNICA
Entropie: 97.4
Salvata in istoric

docker pull denisaaaa/generator-parole:latest
docker run --rm denisaaaa/generator-parole --check pandantiv14
Analiza parolei "pandantiv14":
Putere: PUTERNICA(75/100)
Probleme:
- Prea scurta
- Lipsesc litere mari
- Lipsesc caractere speciale
Sugestii:
- Creste lungimea parolei
- Adauga litere mari
- Adauga caractere speciale