# IDK HOW I BUILT FIN

def play():

    import random

    Fin_wins = 0

    Player_wins = 0

    player_points = 0

    Fin_points = 0

    player_history = {
        "rock":0,
        "scissors":0,
        "paper":0
    }

    counter = {
        "rock":"paper",
        "scissors":"rock",
        "paper":"scissors"
    }

    choices = ("rock","paper","scissors")

    print("YOU WILL BE PLAYING AGAINST FIN :D")

    while True:

        if Player_wins > 1 or Fin_wins > 1:
            player_fav = (max(player_history, key=player_history.get))
            Fin_choice = counter[player_fav]
        else:
            Fin_choice = random.choice(choices)

        your_choice = input("Choose: ")

        if your_choice in choices:
            if your_choice == "rock" and Fin_choice == "scissors" or your_choice == "scissors" and Fin_choice == "paper" or your_choice == "paper" and Fin_choice == "rock":
                print(f"FIN CHOSE: {Fin_choice}")
                player_points += 1
                print("THE SCORE IS:")
                print(f"FIN:{Fin_points} AND PLAYER:{player_points}")
                player_history[your_choice] += 1
                

            elif your_choice == Fin_choice:
                print(f"FIN CHOSE: {Fin_choice}")
                print("ITS A TIE!")
                player_history[your_choice] += 1
            
            else:
                print(f"FIN CHOSE: {Fin_choice}")
                Fin_points += 1
                print("THE SCORE IS")
                print(f"FIN:{Fin_points} AND PLAYER:{player_points} ")
                player_history[your_choice] += 1
        else:
            print("NOT VALID BAHAHAHHAHAHA")

        if player_points >= 3:
            Player_wins += 1
            print("YOU WIN YAY!q")
            print("THE FINAL SCORE IS:")
            print(f"FIN WINS:{Fin_wins} AND YOUR WINS: {Player_wins}")
        
            while True:
                again = input("wanna play again?(Y/N): ").upper()
                if again == "N":
                    return
                elif again == "Y":
                    Fin_points = 0
                    player_points = 0
                    break
                else:
                    print("INVALID INPUT")
                    continue  
        elif Fin_points >= 3:
            Fin_wins += 1
            print("YOU LOST BAHAHAHAHAHAHAH!")
            print("THE FINAL SCORE IS:")
            print(f"FIN WINS:{Fin_wins} AND YOUR WINS: {Player_wins}")
            
            while True:
                again = input("wanna play again?(Y/N): ").upper()
                if again == "N":
                    return
                elif again == "Y":
                    Fin_points = 0
                    player_points = 0
                    break
                else:
                    print("INVALID INPUT")
                    continue