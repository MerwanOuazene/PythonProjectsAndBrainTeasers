import random

def main():
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    guess = [-1, -1, -1, -1]

    def randomize(sequence):
        return random.sample(sequence, 4)

    int_list = randomize(sequence)
    counter = 0

    while True:
        print("Current guess:", guess)
        print("Secret code:", int_list)  # For debugging, remove this in the actual game

        userInput = input("Enter 4 digits (0-9): ")

        if len(userInput) != 4 or not userInput.isdigit():
            print("Invalid input. Please enter exactly 4 digits.")
            continue

        intUserInput = list(map(int, userInput))
        counter += 1

        for i in range(4):
            if int_list[i] == intUserInput[i]:
                guess[i] = intUserInput[i]
            else:
                guess[i] = -1

        if guess == int_list:
            print(f'{guess} was the correct combination, found in {counter} attempts.')
            print('You Win')
            int_list = randomize(sequence)
            guess = [-1, -1, -1, -1]
            counter = 0
        else:
            print("Incorrect guess. Try again.")

if __name__ == "__main__":
    main()
