import random


def main():
  sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  guess = [-1, -1, -1, -1]
  counter = 1

  def randomize(sequence):
    sequence_dict = {
        1: random.choice(sequence),
        2: random.choice(sequence),
        3: random.choice(sequence),
        4: random.choice(sequence)
    }
    return sequence_dict

  values = randomize(sequence)
  print("Dans ce jeu, vous devez trouver une combinaison à 4 chiffres (1234).")
  print("Les chiffres non-trouvés sont symbolisés par -1.")
  print("Vous devez trouver le code secret avec le moins d'essais.")
  print("Début de la partie !")

  while True:
    values_list = list(values.values())
    #print(values_list) cheat code
    userInput = list(map(int, input("Entrez 4 chiffres: ")))
    counter += 1

    if len(userInput) == 4:
      for i in range(4):
        if userInput[i] == values_list[i]:
          guess[i] = userInput[i]
      print(guess)

    if guess == userInput:
      print('gg')
      print(f"La bonne réponse était {guess}")
      print(f"Vous avez trouvé la réponse en {counter} essais!")
      input('"Entrée" pour relancer une partie! ')
      counter = 1
      values = randomize(sequence)
      guess = [-1, -1, -1, -1]


if __name__ == "__main__":
  main()
