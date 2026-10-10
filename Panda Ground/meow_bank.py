def start():

    import json

    file_path = "C:/Users/TLS/Downloads/python/Panda Ground/PandaGround_DataCenter.json"


    def account_file():
        with open(file_path, "r") as file:
            account = json.load(file)
            account_info = account["bank_account"]
        return account

    account_file()

    account = account_file()

    def write_file():
        with open(file_path, "w") as file:
            json.dump(account, file, indent=4)

    def deposit():
        Verify_PIN = str(input("Enter your T-PIN: "))
        if Verify_PIN == account["T-PIN"]:
            amount = float(input("Enter the amount you want to deposit: "))
            if amount <= 0:
                print("Deposit amount must be greater than zero.")
                return
            else:
                account["Balance"] += amount
                write_file()
                print(f"Deposit successful! Your new balance is: {account['Balance']}")
        else:
            print("Incorrect T-PIN.")

    def withdraw():
        Verify_PIN = str(input("Enter your T-PIN: "))
        if Verify_PIN == account["T-PIN"]:
            amount = float(input("Enter the amount you want to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
                return
            elif amount > 0 and amount <= account["Balance"]:
                account["Balance"] -= amount
                write_file()
                print(f"Withdrawal successful! Your new balance is: {account['Balance']}")
            else:
                print("Insufficient funds.")
        else:
            print("Incorrect T-PIN.")

    def shutdown():
        print("Shutting down...")
        return()

    def account_creation():
        print("--------------------------")
        print("YOU DO NOT HAVE A ACCOUNT")
        print("CREATE AN ACCOUNT TO BE ABLE")
        print("TO USE THIS PROGRAM")
        print("--------------------------")
        while True:
            ask = str(input("Would you like to create an account? (y/n): ")).lower()
            if ask == "n":
                break
            elif ask == "y":
                while True:
                    Username = str(input("Make an username : "))
                    Password = str(input("Make a password (should be atleast 5 characters long): "))
                    T_PIN = str(input("Enter your T-PIN (cannot be longer than 4 numbers): "))
                    if len(Password) < 5 or len(T_PIN) > 4:
                        print("INVALID T-PIN OR PASSWORD")
                        continue
                    else:
                        account.update({"Name": Username})
                        account.update({"Password": Password})
                        account.update({"T-PIN": T_PIN})
                        write_file()
                        return

    running = True

    commands = {
        "echeck_balance": lambda: print(f"Your balance is: {account['Balance']}"),
        "edeposit": deposit,
        "ewithdraw": withdraw,
        "exit": shutdown,
        "instructions": lambda: print(
            "Available commands:\n- echeck_balance: Check your balance\n- edeposit: Deposit money\n- ewithdraw: Withdraw money\n- instructions: Show this message\n- exit: Exit the program"
        ),
    }

    while running:
        if account["Name"] is None or account["Password"] is None or account["T-PIN"] is None:
            account_creation()
        else:
            print("WELCOME TO MEOW BANK")
            print(account["Balance"])
            choice = input("What would you like to do: ")
            if choice in commands:
                commands[choice]()
            else:
                print("Invalid input")
                continue