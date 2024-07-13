import random 

def main():
    
    rps = {
        "Scissors" : "Paper",
        "Paper" : "Rock",
        "Rock" : "Scissors"
    }

    def who_wins(A, B, rps):
        if A == B:
            print(f"Tie, you both chose {A}")
        elif rps[A] == B:
            print(f"You Win, CPU chose {B}")
        elif rps[B] == A:
            print(f"You Lose, CPU chose {B}")

    print("LANCEMENT DU JEU")
    while True:
        
        userInput = input("Choose Rock, Paper or Scissors : ").capitalize()
        cpuChoice = random.choice(list(rps.keys()))

        if userInput in list(rps.keys()):
            who_wins(userInput, cpuChoice, rps)
        else:
            print("CHOOSE ROCK, PAPER OR SCISSORS IDIOT")

if __name__ == "__main__":
    main()