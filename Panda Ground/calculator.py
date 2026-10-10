def start():

   while True: 
    numbers = []
    answer = float(input("Enter your first number: "))
    
    while True:
        main_numbers = float(input("Enter your number: "))
        numbers.append(main_numbers)
        End = input("Wanna add another number? (Y/N): ").lower()
        if End == "y":
            continue
        elif End == "n":
            break

    question3 = input("enter what you want to do (+,-,*,/): ")

    if question3 == "+":
        for number in numbers:
            answer += number
        print(answer)

    elif question3 == "-":
        for number in numbers:
            answer -= number
        print(answer)
    
    elif question3 == "*":
        for number in numbers:
            answer *= number
        print(answer)

    elif question3 == "/":
        for number in numbers:
            answer /= number
        print(answer)

    else:
        print("THATS NOT AN OPTION")

    while True:
        question4 = input("WANNA DO ANOTHER CALCULATION? :D (Y/N):").lower()

        if question4 == "y":
            break
        elif question4 == "n":
            return
        else:
            print("THATS NOT AN OPTION")