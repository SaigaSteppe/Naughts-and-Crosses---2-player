import random
def board(tile):
    print(tile[7]+"|"+tile[8]+"|"+tile[9])
    print("-+-+-")
    print(tile[4]+"|"+tile[5]+"|"+tile[6])
    print("-+-+-")
    print(tile[1]+"|"+tile[2]+"|"+tile[3])
    
def display_rules():
    print("Player 1 is \"X\" and Player 2 is \"O\"")

def check_win(positions):
##win = (1,2,3) or (4,5,6) or (7,8,9) or (7,4,1) or (8,5,2) or (9,6,3) or (7,5,3) or (9,5,1)
    return (((1 in positions) and (2 in positions) and (3 in positions)) or\
            ((4 in positions) and (5 in positions) and (6 in positions)) or\
            ((7 in positions) and (8 in positions) and (9 in positions)) or\
            ((7 in positions) and (4 in positions) and (1 in positions)) or\
            ((8 in positions) and (5 in positions) and (2 in positions)) or\
            ((9 in positions) and (6 in positions) and (3 in positions)) or\
            ((7 in positions) and (5 in positions) and (3 in positions)) or\
            ((9 in positions) and (5 in positions) and (1 in positions)))
            
             #e.g. False,False,True --> False
             #     True,True,True --> True                      

def game(tile):
    available = [1,2,3,4,5,6,7,8,9]
    player1_positions = []
    player2_positions = []
    turn_count = 1

    while True:
        try:
            #Player 1's turn
            if turn_count % 2 != 0:
                print("="*30)
                print("Player 1's(X) turn")
                player1_choice = int(input("Enter a position: "))
                if player1_choice == 0 or player1_choice in player2_positions or player1_choice in player1_positions:
                    raise Exception
                tile[player1_choice] = "X"
                player1_positions.append(player1_choice)
                available.pop(available.index(player1_choice))

            #Player 2's turn
            if turn_count % 2 == 0:
                print("="*30)
                print("Player 2's(O) turn")
                player2_choice = int(input("Enter a position: "))
                if player2_choice == 0 or player2_choice in player1_positions or player2_choice in player2_positions:
                    raise Exception
                tile[player2_choice] = "O"
                player2_positions.append(player2_choice)
                available.pop(available.index(player2_choice))
    
            turn_count += 1    
            board(tile)
            print("\nPlayer 1(X):",player1_positions)
            print("Player 2(O):",player2_positions)

            #check win
            if check_win(player1_positions) == True:
                print("PLAYER 1 WINS!")
                break
            if check_win(player2_positions) == True:
                print("PLAYER 2 WINS!")
                break
            if available == [] and check_win(player1_positions) == False and check_win(player2_positions) == False:
                print("DRAW!")
                break
        except:
            print("\nINVALID INPUT.")
            board(tile)
            print("\nPlayer(X):",player1_positions)
            print("player2(O):",player2_positions)
            if check_win(player1_positions) == True:
                print("PLAYER 1 WINS!")
                break
            if check_win(player2_positions) == True:
                print("PLAYER 2 WINS!")
                break
            if available == [] and check_win(player1_positions) == False and check_win(player2_positions) == False:
                print("DRAW!")
                break

    prompt_replay = int(input("\nTo play again, enter [1]: \n"))
    if prompt_replay == 1:
        print("*"*30,"\n")
        main()
def main():
    tile = [None,"1","2","3","4","5","6","7","8","9"]
    board(tile)
    display_rules()
    game(tile)
    
main()
