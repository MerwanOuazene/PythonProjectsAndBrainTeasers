import random

def main():
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    guess = ['_', '_', '_', '_']

    def randomize(sequence):
        int_dict = {1: random.choice(sequence),
            2: random.choice(sequence),
            3: random.choice(sequence),
            4: random.choice(sequence)}
        return int_dict
    

    int_dict = randomize(sequence)
    list_values = list(int_dict.values())
    list_values = [int(i) for i in list_values]

    while True:
        print(f"Solution is {list_values}")
        userInput = list(input("Entrez un nombre entre 0000 et 9999: "))
        userInput = [int(i) for i in userInput]
        for value in userInput:
            input_index = userInput.index(value)
            if userInput[input_index] == list_values[input_index]:
                guess[input_index] = userInput[input_index]
            else:
                print(guess)
        print(guess)



if __name__ == "__main__":
    main()