#rock_paper_scissors.py
def play():

    import random 

    print("You will be playing against Fin the shark >:D")

    choices = ("rock", "paper", "scissors")

    player_history = {
        "rock":0,
        "paper":0,
        "scissors":0
    }

    second_moves = {
        "rock":0,
        "paper":0,
        "scissors":0
    }

    counter = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }

    player_score = 0
    Fin_score = 0


    player_wins = 0
    Fin_wins = 0

    while True:

        if player_wins > 0 or Fin_wins > 0:
            most_used = max(player_history, key=player_history.get)
            Fin_options = (random.choice(choices),counter[most_used])
            Fin_choice = random.choice(Fin_options)
        else:
            Fin_choice = random.choice(choices)


        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

        if player_choice == "quit":
            break
        
        elif player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        print(f"Fin chose: {Fin_choice}")
        
        if player_choice == Fin_choice:
            print("It's a tie!")
            player_history[player_choice] += 1
        


        elif (player_choice == "rock" and Fin_choice == "scissors") or \
            (player_choice == "paper" and Fin_choice == "rock") or \
            (player_choice == "scissors" and Fin_choice == "paper"):
            
            player_history[player_choice] += 1
            127

            print("You win!")
            player_score += 1

        else:
            print("Fin wins!")
            Fin_score += 1
            player_history[player_choice] += 1
        


        if player_score > 2:
            player_wins +=1

            print(f"YOUR WINS:{player_wins} AND FIN'S WINS:{Fin_wins}")

            print("You won the game! Congratulations!")

            player_score = 0
            Fin_score = 0

            while True:
                retry = input("Press R to continue or type 'quit' to exit: ").upper()

            
                if retry == "R":
                    break

                elif retry == "QUIT":
                    break

                else:
                    print("Invalid input. Please try again.")
            
            if retry == "QUIT":
                    break
                

        elif Fin_score > 2:
            Fin_wins +=1
            print("Fin won the game! Better luck next time!")

            print(f"YOUR WINS:{player_wins} AND FIN'S WINS:{Fin_wins}")

            player_score = 0
            Fin_score = 0

            retry = input("Press R to continue or type 'quit' to exit: ").upper()

            if retry == "QUIT":
                break
            elif retry == "R":
                continue
            else:
                print("invalid input")
            