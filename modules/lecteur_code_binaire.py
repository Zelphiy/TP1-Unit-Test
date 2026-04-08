from modules.code_binaire import CodeBinaire
from modules.bit import Bit


class LecteurCodeBinaire:

    @staticmethod
    def depuis_input_utilisateur():
        chaine = input("Entrez une chaîne binaire (0 et 1) : ").strip()
        return LecteurCodeBinaire._parse_chaine_binaire(chaine)
    
    @staticmethod
    def depuis_fichier(nom_fichier):
        try:
            with open(nom_fichier, 'r') as f:
                chaine = f.read().strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"Le fichier '{nom_fichier}' n'existe pas.")
        
        return LecteurCodeBinaire._parse_chaine_binaire(chaine)
    
    @staticmethod
    def _parse_chaine_binaire(chaine):
        if not chaine:
            raise ValueError("La chaîne binaire ne peut pas être vide.")
        
        if not all(c in '01' for c in chaine):
            raise ValueError("La chaîne doit contenir uniquement des '0' et des '1'.")
        
        bits = [Bit.BIT_0 if c == '0' else Bit.BIT_1 for c in chaine]
        return CodeBinaire(*bits)
