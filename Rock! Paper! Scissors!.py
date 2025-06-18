# R, P, S
# 0, 1, 2

while True:
    import random as rd

    Options = {0: 2, 1: 0, 2: 1}
    Results = [0, 1, 2]
    Result = 0

    # Word = wrd
    ply_choice = {"rock": 0, "paper": 1, "scissor": 2}
    wrdOptions = {0: "Rock", 1: "Paper", 2:"Scissor"}
    wrdResults = {0: "Win", 1:"Lose", 2: "Draw"}

    print("Welcome to Rock Paper Scissors!\nChoose between rock/paper/scissors")

    # Choice
    choice = str(input("Your Choice: "))
    if choice != "":
        player_choice = ply_choice.get(choice)

        comp_choice = int(rd.choice(list(Options.keys())))

        # Win/Lose/Draw
        if comp_choice == player_choice:
            Result = 2

        elif Options.get(comp_choice) == player_choice:
            Result = 1

        else:
            Result = 0

        # GUI 
        print(f"Computer's Choice: {wrdOptions.get(comp_choice)}")
        print(wrdResults.get(Result))
        print()

    if choice == "":
        print("Please choose a choice!\n")