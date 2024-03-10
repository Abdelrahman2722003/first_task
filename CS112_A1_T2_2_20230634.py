#File:scrabble game
#Purpose:play with a list of numbers from 1 to 9 each player has pick a number from list,once a number has been picked,it cannont be picked again,if player picked 3 numbers that added up to 15 he win, however if all numbers used with no winner it will end draw
#Author:Abelrahman mohamed ramadan
#ID:20230634

from itertools import combinations

def check_the_winner(list_of_numbers):          #to check all posible combination of 3 numbers and check thier sum
    for i in combinations(list_of_numbers, 3):
        if sum(i) == 15:            #if combination of any 3 numbers equal 15 retun tru
            return True
    return False

def display_game_status(list_of_numbers, player_1_numbers, player_2_numbers):           #to display status of the game in each turn
    print("The remaining numbers:", list_of_numbers)
    print("Player 1 numbers:", player_1_numbers)
    print("Player 2 numbers:", player_2_numbers)

list_of_numbers = list(range(1, 10))
player_1_numbers = []
player_2_numbers = []
turn = 0

while turn < 9:         #the main loop
    display_game_status(list_of_numbers, player_1_numbers, player_2_numbers)

    pick = input("PLAYER 1 TURN: Pick a number from 1 to 9: ")
    if not pick.isdigit() or int(pick) not in list_of_numbers:  #check validity of the input wheather if input not a number or input is a number but not in the list
        print("Please enter a valid number from the list.")
        continue
    pick = int(pick)
    player_1_numbers.append(pick)           #add the input to player 1 numbers
    list_of_numbers.remove(pick)            #remover this number from the list

    if check_the_winner(player_1_numbers):          #to check if player 1 wins
        print("congratulations!\n ******** Player 1 is the winner! ********")
        display_game_status(list_of_numbers, player_1_numbers, player_2_numbers)
        break
    turn += 1
    if turn == 9:
        print("Draw")           #if value of turn=9 it means all numbers is picked from the list and no one win, then it is a draw
        break
    display_game_status(list_of_numbers, player_1_numbers, player_2_numbers)

#and here we just will repeat this steps again but with player 2

    pick = input("PLAYER 2 TURN: Pick a number from 1 to 9: ")
    if not pick.isdigit() or int(pick) not in list_of_numbers:
        print("Please enter a valid number from the list.")
        continue
    pick = int(pick)

    if pick in player_2_numbers:
        print("You have already picked this number.")
        continue
    player_2_numbers.append(pick)
    list_of_numbers.remove(pick)

    if check_the_winner(player_2_numbers):
        print("congratulations!\n ******** Player 2 is the winner! ********")
        display_game_status(list_of_numbers, player_1_numbers, player_2_numbers)
        break
    turn += 1
    display_game_status(list_of_numbers, player_1_numbers, player_2_numbers)