from modules.lecteur_code_binaire import LecteurCodeBinaire

print("=== Exemple 1: Lecture depuis un fichier ===")
try:
    code = LecteurCodeBinaire.depuis_fichier('exemple_binaire.txt')
    print(f"Code binaire depuis fichier: {code}")
    print(f"Représentation: {repr(code)}")
    print(f"Longueur: {len(code)}")
except FileNotFoundError as e:
    print(f"Erreur: {e}")

print("\n=== Exemple 2: Création directe ===")
try:
    code = LecteurCodeBinaire._parse_chaine_binaire("11001100")
    print(f"Code binaire: {code}")
    print(f"Représentation: {repr(code)}")
except ValueError as e:
    print(f"Erreur: {e}")

print("\n=== Exemple 3: Chaîne invalide ===")
try:
    code = LecteurCodeBinaire._parse_chaine_binaire("1101a1")
    print(f"Code binaire: {code}")
except ValueError as e:
    print(f"Erreur attendue: {e}")

print("\n=== Exemple 4: Chaîne vide ===")
try:
    code = LecteurCodeBinaire._parse_chaine_binaire("")
    print(f"Code binaire: {code}")
except ValueError as e:
    print(f"Erreur attendue: {e}")

print("\n=== Exemple 5: Opérations sur CodeBinaire ===")
code1 = LecteurCodeBinaire._parse_chaine_binaire("101")
code2 = LecteurCodeBinaire._parse_chaine_binaire("110")
print(f"Code 1: {code1}")
print(f"Code 2: {code2}")
print(f"Concaténation: {code1 + code2}")
print(f"Accès à l'index 0: {code1[0]}")
print(f"Slice [0:2]: {code1[0:2]}")
