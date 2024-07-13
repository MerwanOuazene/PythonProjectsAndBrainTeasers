import random

def main():
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    guess = [-1, -1, -1, -1]

    def randomize(sequence):
        int_dict = {
            1: random.choice(sequence),
            2: random.choice(sequence),
            3: random.choice(sequence),
            4: random.choice(sequence)
        }
        return int_dict

    int_dict = randomize(sequence)
    counter = 0

    while True:
        list_values = list(int_dict.values())
        print(list_values)
        
        userInput = list(input("Entrez 4 chiffres : "))
        counter += 1
        
        intUserInput = list(map(int, userInput))
        
        for value in range(0, len(list_values)):
            for _ in range(0, len(list_values)):
                if list_values[value] == intUserInput[value]:
                    guess[value] = intUserInput[value]
                    
                    if guess == list_values:
                        print(f'{guess} était la bonne combinaison, trouvée en {counter} essais')
                        print('You Win')
                        int_dict = randomize(sequence)
                        guess = [-1, -1, -1, -1]
                        counter = 0
                    break
        print(guess)


if __name__ == "__main__":
    main()
