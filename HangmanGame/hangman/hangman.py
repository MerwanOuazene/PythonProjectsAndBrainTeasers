import random

def main():
    listOfWords = ["abandonner", "abeille", "abri", "accident", "acheter", "action", "addition", "adieu", "admettre", "affaire",
    "bagage", "baguette", "bain", "baiser", "balayer", "baleine", "banane", "banc", "bande", "banque", "balader",
    "cabane", "cacher", "cadeau", "café", "caisse", "calculer", "calme", "camion", "campagne", "canard",
    "dame", "danger", "danser", "date", "débattre", "décider", "décrire", "défendre", "déjeuner", "demander",
    "eau", "école", "écrire", "écouter", "éducation", "effet", "effort", "égal", "église", "élève",
    "fabriquer", "facile", "facteur", "faim", "falloir", "famille", "farine", "fatigue", "faut", "féliciter",
    "gagner", "garder", "gâteau", "gauche", "geler", "gendarme", "général", "génie", "gentil", "geste",
    "habiller", "habiter", "habitude", "haie", "haine", "heure", "histoire", "hiver", "homme", "honnête",
    "idée", "ignorer", "il", "image", "imaginer", "immense", "important", "impossible", "impression", "incendie",
    "jamais", "jambe", "janvier", "jardin", "jaune", "jeter", "joie", "jouer", "jour", "journal",
    "kaki", "kilo", "kilomètre", "kiwi", "koala", "kyste",
    "laver", "légume", "lent", "lèvre", "libre", "lire", "livre", "loger", "loin", "lumière",
    "machine", "magasin", "main", "maison", "manger", "marcher", "matin", "médecin", "mer", "mettre",
    "nager", "neige", "nettoyer", "neuf", "noble", "nom", "nombre", "noir", "noter", "nouveau",
    "objet", "obliger", "observer", "obtenir", "océan", "odeur", "offrir", "ombre", "onze", "ouvrir",
    "pain", "parler", "partir", "passer", "patience", "payer", "peine", "penser", "perdre", "personne",
    "quand", "quart", "quatorze", "quatre", "quitter", "quoi",
    "radio", "raison", "ramasser", "rapide", "rappeler", "recevoir", "recherche", "recommencer", "réfléchir", "refuser",
    "sac", "sage", "saison", "saluer", "sang", "santé", "savoir", "secouer", "sel", "sentir",
    "table", "taille", "taire", "taper", "temps", "tenir", "terre", "tête", "tirer", "tourner",
    "utile", "utiliser",
    "vache", "valise", "valoir", "vanter", "vendre", "venir", "vent", "verre", "vêtements", "vie",
    "wagon", "wagonnet", "wallon", "whisky", "wifi",
    "xénophobe", "xénope", "xérès", "xérographie", "xylophone",
    "yaourt", "yacht", "yoga", "yo-yo", "youpi",
    "zèbre", "zèle", "zéro", "zigzag", "zoo"]
  
    while True:

        hangman_word = random.choice(listOfWords).upper()
        hangCounter = 0
        hangDifficulty = 8
        failedLetters = set()

        print("Début du pendu")
        print(f"Le mot choisi est de {len(hangman_word)} lettres")
            
        hangman_hyphen = ["_" for x in range(0, len(hangman_word))]
    
        while ''.join(hangman_hyphen) != hangman_word:
            if len(failedLetters) != 0:
                print(f"Lettres testées : {failedLetters}")
            print("Entrez une lettre :")

            guessedLetter = input("").capitalize()
            if guessedLetter in hangman_word and guessedLetter not in failedLetters:
                print(f'La lettre {guessedLetter} est dans le mot !')
                for letter in range(0, len(hangman_word)):
                        if hangman_word[letter] == guessedLetter:
                            hangman_hyphen[letter] = guessedLetter
                print(hangman_hyphen)

            
            else:
                if guessedLetter not in failedLetters:
                    hangCounter +=1
                    failedLetters.add(guessedLetter)
                    print(f"La lettre {guessedLetter} n'est pas dans le mot, vous perdez une vie")
                    print(f"Il vous reste {hangDifficulty - hangCounter} vies")
                print(hangman_hyphen)
                
                if hangCounter == hangDifficulty:
                    print("Perdu!")
                    print(f"Le mot était {hangman_word}")
                    print("------------------")
                    return

        print('Gagné!!')
        print(f'Le mot était {hangman_word}')
        print(f"Il vous restait {hangDifficulty - hangCounter} vies!")
        print("------------------")
            

    
        

if __name__ == "__main__":
    main()
