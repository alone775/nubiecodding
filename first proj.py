revive = 1
endgame = ""
while (endgame != "yes "):

    a = input("Pick up a sword press Y/N :")
    if (a == "y"):
        print("pick a mod to kill")
        print("a goblin")
        c = input("Y to kill this goblin :")
        if (c == 'y'):
            print("u have successfully killed a Goblin")
        else:
            print("ur killed by that goblin ")
            j = input("write revive to get a revive :")
            if (j == 'revive'):
                print(f"u are back in the game for the {revive} time ")
                revive += 1
        l = input("to kill this dangerous wolf enter Y to kill :")
        if (l == 'y'):
            print("you have successfully killed this dangerous wolf if it wasnt for u it  was going to kill every one in the village here are ur rewards ")
        else:
            print("You have died again u only have 1 life left ")
            g = input(f"enter revive for the {revive} time :")
            if (g == 'revive'):
                i = input(
                    f"ur back in the game its ur {revive} if u mess up its game over for u ")
        d = input(
            "the village is in need of u can u help us with the delivery job to the capital : Y/N :")
        if (d == 'y'):
            print("great lets get ready and rolling as soon as possible ")
            d = input(
                "later that evening traveling we encounter a dragon u and the other adventurers are the last hope do u want to help them Y/N :")
            if (d == 'y'):
                print("u guys tried but u all died trying to defeat it .")
                print("-"*100)
                print("do u want to play again or end game ?")
                endgame = input(
                    "enter 'yes' if u want to end the game ")
            elif (d == "n"):
                # This line of code is printing a message to the player indicating that they and their
                # fellow adventurers did not even try to defeat the dragon and as a result, they all
                # died a miserable death. The message also includes some taunting language, calling
                # the player a coward and challenging them to try again if they are brave enough.
                print("u guys didn't even tried and u all died a miserable death buy the dragons hand u could at'least tried to stop it maybe u would have succeded coword try again if u brave enough.")
                print("-"*100)
                print("do u want to play again or end game ?")
                endgame = input(
                    "enter 'yes' if u want to end the game ")

    else:
        print("noob why did u even spawn if u dont even want to hold a sword lol")
