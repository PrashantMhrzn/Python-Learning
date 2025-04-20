# sessior, paper, rock
# there are two players
# ask player 1 (s,p,r)
# ask player 2 (s,p,r)
# if input of both player are same print tie
# if player 1 input is rock and player 2 input is paper, print player 2 wins
# if player 1 input is rock and player 2 input is sessior, print player 1 wins
# if player 1 input is paper and player 2 input is sessior, print player 2 wins

# ask if they want to continue, if yes continue the game, else exit the game


while True:
    print("Player 1>")
    player1 = input("Scissor, Paper, Rock!(s, p, r): ")
    print("Player 2>")
    player2 = input("Scissor, Paper, Rock!(s, p, r): ")

    if player1 == player2:
        print('Its a TIE!')
    # Player 1 win conditions
    elif player1 == 'p' and player2 == 'r':
        print("Player1 Wins!")
    elif player1 == 's' and player2 == 'p':
        print("Player1 Wins!")
    elif player1 == 'r' and player2 == 's':
        print("Player1 Wins!")
    # Player 2 win conditions
    elif player2 == 'p' and player1 == 'r':
        print("Player2 Wins!")
    elif player2 == 's' and player1 == 'p':
        print("Player2 Wins!")
    elif player2 == 'r' and player1 == 's':
        print("Player2 Wins!")
    else:
        print("Invalid input")

    # Continue or end loop as per y or n
    con = input("Do you want to continue?[y/n]: ")
    if con == 'y':
        continue
    elif con == 'n':
        break
    else:
        print('Invalid input!')
        break