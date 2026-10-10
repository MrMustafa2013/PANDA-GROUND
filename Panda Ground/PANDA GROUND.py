import json
import webbrowser
import calculator
import rock_paper_scissors
import meow_bank

file_path = "C:/Users/TLS/Downloads/python/Panda Ground/PandaGround_DataCenter.json"

apps = {
    "calculator": calculator,
    "meow bank": meow_bank
}

games = {"rock paper scissors": rock_paper_scissors}

def load():
    global links, user , bank_account
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            links = data["links"]
            user = data["user"]
            bank_account = data["bank_account"]
    except Exception as e: 
        print(f"Error loading data: {e}")

def save():
    global links, user, bank_account
    try:
        Data = {
            "links": links,
            "user": user,
            "bank_account": bank_account
        }
        with open(file_path, "w") as file:
            json.dump(Data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def add():
    name = input("Enter the website's name: ")
    new = input("Copy paste your link here: ")

    if len(links) >= 3 and user.get("status") == "free":
        print("You have reached the maximum number of websites you can add :/")
        print("You can either remove a website OR buy premium to have infinite websites AND BE SUPER COOL :P")
        buy_premium = input("Do you want to buy premium? (Y/N): ").upper()
        if buy_premium == "Y":
            premium()
        elif buy_premium == "N":
            print("Awh no premium bamboo for tonight then :(")
        else:
            print("ERROR U R ANNOYING: READ THE FUCKING TEXT YOU DUMBASS")
    else:
        links.update({name: new})
        save()
        print("Your website has been installed :P")
        print("-------------------")
        print("AVAILABLE WEBSITES:")
        for keys in links:
            print(f"{keys}")
        print("-------------------")

def open_apps():
    print("-------------------")
    print("AVAILABLE APPS:")
    for keys in apps:
        print(f"{keys}")
    print("-------------------")
    app_choice = input("Which app would you like to open: ").lower()
    if app_choice in apps:
        apps[app_choice].start()
    else:
        print("ERROR 404:APP NOT FOUND")

def open_games():
    print(
        "UPDATE GOLDEN APPLE (version 2.0) HAS INTRODUCED PANDA GROUND'S OWN GAMES! :D"
    )

    print("Available games:")
    for g in games:
        print(f"{g}")
    game_choice = input("\nType the name of the game you want to play: ").lower()
    if game_choice in games:
        games[game_choice].play()
    else:
        print("ERROR 404:GAME NOT FOUND")

def websites():
    print("-------------------")
    print("AVAILABLE WEBSITES:")
    for keys in links:
        print(f"{keys}")
    print("-------------------")
    website_choice = input("Choose a website you want to open: ")
    if website_choice in links:
        webbrowser.open(links[website_choice])
    else:
        print("Error 404:WEBSITE NOT FOUND")

def shutdown():
    while True:
        print("Panda Ground has been closed")
        reopen = input("Wanna launch Panda Ground? (Y): ").upper()
        if reopen == "Y":
            break
        else:
            continue

def updates():
    updates = (
        "UPDATE COCONUT (V1.5)",
        "UPDATE GOLDEN APPLE (V2.0)",
    )
    for u in updates:
        print(u)

    Versions = {
        "GOLDEN APPLE(V2.0)": [
            "UPDATE GOLDEN APPLE(V2.0)",
            "WE HAVE GAMES NOW >:D",
            "WE DO NOT DEPEND ON GOOGLE'S CALCULATOR ANYMORE",
            "WE HAVE OUR OWN BANK NOW :D",
            "WE HAVE PREMIUM NOW WHICH GIVES YOU INFINITE WEBSITES YAY!"
            "YOUR WEBSITES ARE STORED FOREVER NOW YAY!"
        ],
        "COCONUT(V1.5)": [
            "UPDATE COCONUT(V1.5)",
            "You can now add/remove any website now! :D",
        ],
    }

    abt_update = input("Type name(version) to learn about an update: ").upper()

    if abt_update in Versions:
        for line in Versions[abt_update]:
            print(line)
    else:
        print("This update does not exist :/")

def instructions():
    print("Press X to exit the program")
    print("Type add to add a new website")
    print("To check the latest update type updates")
    print("To remove a website type remove")
    print("type apps to access available apps")
    print("To access the available websites type websites")
    print("To access the available games type games")

def remove():
    choose = input("Do you want to remove a website or a game? (w/g): ")

    if choose == "w":
        website = input("Enter the website's name you want to remove: ")
        if website in links:
            links.pop(website)
            save()
            print(f"{website} has been removed from the list.")
            print("-------------------")
            print("AVAILABLE WEBSITES:")
            for keys in links:
                print(f"{keys}")
            print("-------------------")
        else:
            print("ERROR 404: WEBSITE NOT INSTALLED")

    elif choose == "g":
        game = input("Enter the game's name you want to remove: ").lower()
        if game in games:
            games.pop(game)
            print(f"{game} has been removed from the list.")
            print("-------------------")
            print("AVAILABLE GAMES:")
            for g in games:
                print(f"{g}")
            print("-------------------")
        else:
            print("ERROR 404: GAME NOT FOUND")

def premium():
    print("To buy premium add your bank account details: ")
    name = input("Enter your name: ")
    t_pin = int(input("Enter your T-PIN: "))
    password = int(input("Enter your password: "))  

    if name == bank_account["Name"] and t_pin == bank_account["T-PIN"] and password == bank_account["Password"]:
        print("Premium costs $5.00 ")
        print("Type confirm to buy premium and be the coolest creature ever :p")
        print("or type cancel to cancel the purchase and be show how broke you are :/")
        buying = input("").lower()
        if buying == "confirm":
            if bank_account["Balance"] >= 5.00:
                bank_account["Balance"] -= 5.00
                print("You have successfully bought premium! :D")
                print("YOU ARE NOW SUPER COOL AND CAN ADD INFINITE AMOUNT OF WEBSITES")
                user["status"] = "premium"
                save()
                return
            else:
                print("You don't have enough money for premium :(")
    else:
        print("DOES NOT MATCH YOUR INFOMARTION")

commands = {
    "add": add,
    "games": open_games,
    "apps": open_apps,
    "websites": websites,
    "x": shutdown,
    "updates": updates,
    "i": instructions,
    "remove": remove,
    "buy premium": premium
}

load()

print("Welcome to Panda Ground OS V2.0 :D")
print("type i for instructions")

while True:
    choice = input("what do you wanna do? :D: ").lower()
    if choice in commands:
        commands[choice]()
    else:
        print("ERROR IDIOT: YOU ARE THE REASON I ADDED INSTRUCTIONS :/")